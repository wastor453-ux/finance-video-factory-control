#!/usr/bin/env python3
"""Simulated takeover test on a temp copy of the repo (the real repo is never modified).
Claude-A hits a limit -> Claude-B takes over and finishes -> Claude-A resumes."""
import hashlib, os, re, shutil, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_repo import check
from build_briefing import build

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ok = []


def step(name, cond, detail=""):
    ok.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (f" -- {detail}" if detail and not cond else ""))


def rd(p):
    with open(p, encoding="utf8") as f:
        return f.read()


def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf8") as f:
        f.write(s)


def refresh(repo):
    wr(os.path.join(repo, "BRIEFING.md"), build(repo))


def sha(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def handoff(who, prev, done, nxt):
    return f"# Handoff by {who}\nPrevious handoff: [{prev}]({prev})\n## Done (with evidence)\n- {done}\n## Next action\n- {nxt}\n"


def main():
    tmp = tempfile.mkdtemp()
    repo = os.path.join(tmp, "repo")
    shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    hd = os.path.join(repo, "HANDOFFS")
    base = sorted(n for n in os.listdir(hd) if n != "LATEST.md")
    base_hash = {n: sha(os.path.join(hd, n)) for n in base}
    step("0. baseline repo passes the structure check", check(repo) == [], "; ".join(check(repo)))

    wr(os.path.join(repo, "JOBS/doing/TEST-0001.md"), "# TEST-0001\nStatus: DOING\nAssignee: Claude\nTask: report part 1 and part 2.\n")
    wr(os.path.join(repo, "JOBS/todo/TEST-0002.md"), "# TEST-0002\nStatus: TODO\nAssignee: Muse\nTask: apply patch (Muse only).\n")
    muse_before = sha(os.path.join(repo, "JOBS/todo/TEST-0002.md"))

    wr(os.path.join(repo, "TESTWORK/report.md"), "part 1 done by Claude-A\n")
    n1 = "2026-12-01-01-claude-a.md"
    wr(os.path.join(hd, n1), handoff("Claude-A", base[-1], "report part 1 (TESTWORK/report.md)", "write report part 2 (TEST-0001); Muse owns TEST-0002"))
    shutil.copy(os.path.join(hd, n1), os.path.join(hd, "LATEST.md"))
    refresh(repo)
    step("1. Claude-A handoff written, structure valid", check(repo) == [], "; ".join(check(repo)))

    latest = rd(os.path.join(hd, "LATEST.md"))
    done = re.search(r"## Done.*?\n- (.+)", latest, re.S).group(1)
    nxt = re.search(r"## Next action\n- (.+)", latest).group(1)
    step("2a. Claude-B identifies completed work", "part 1" in done)
    step("2b. Claude-B identifies the exact next action", "part 2" in nxt and "TEST-0001" in nxt)
    st = rd(os.path.join(repo, "STATUS.md"))
    wr(os.path.join(repo, "STATUS.md"), re.sub(r"^LOCK:.*$", "LOCK: HELD by Claude-B since test; job TEST-0001", st, flags=re.M))
    refresh(repo)
    step("2c. Claude-B takes the lock and the structure stays valid", check(repo) == [], "; ".join(check(repo)))
    wr(os.path.join(repo, "TESTWORK/report.md"), rd(os.path.join(repo, "TESTWORK/report.md")) + "part 2 done by Claude-B\n")
    n2 = "2026-12-01-02-claude-b.md"
    wr(os.path.join(hd, n2), handoff("Claude-B", n1, "report part 2 (TESTWORK/report.md)", "Claude-A resumes; Muse applies patch (TEST-0002)"))
    shutil.copy(os.path.join(hd, n2), os.path.join(hd, "LATEST.md"))
    wr(os.path.join(repo, "STATUS.md"), re.sub(r"^LOCK:.*$", "LOCK: FREE", rd(os.path.join(repo, "STATUS.md")), flags=re.M))
    refresh(repo)
    step("2d. Claude-B handoff valid, links to A's, lock freed", check(repo) == [], "; ".join(check(repo)))

    latest = rd(os.path.join(hd, "LATEST.md"))
    rep = rd(os.path.join(repo, "TESTWORK/report.md"))
    step("3a. Claude-A reads Claude-B's handoff as newest", "by Claude-B" in latest)
    step("3b. nothing redone: part 1 once, part 2 present", rep.count("part 1 done") == 1 and "part 2 done" in rep)
    step("3c. Claude-A sees the remaining task is Muse's", "Muse applies patch" in latest)

    step("4a. no earlier handoff changed or deleted", all(os.path.exists(os.path.join(hd, n)) and sha(os.path.join(hd, n)) == h for n, h in base_hash.items()))
    step("4b. both new handoffs preserved", os.path.exists(os.path.join(hd, n1)) and os.path.exists(os.path.join(hd, n2)))
    step("4c. Muse's job file unchanged", sha(os.path.join(repo, "JOBS/todo/TEST-0002.md")) == muse_before)
    step("3d. a chat-only Claude gets the newest state from BRIEFING.md alone", "by Claude-B" in rd(os.path.join(repo, "BRIEFING.md")) and "TEST-0002" in rd(os.path.join(repo, "BRIEFING.md")))
    step("4d. final structure check", check(repo) == [], "; ".join(check(repo)))
    shutil.rmtree(tmp)
    print(f"\n{sum(ok)}/{len(ok)} checks passed")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main())
