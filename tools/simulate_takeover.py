#!/usr/bin/env python3
"""Simulated takeover test on a temp copy of the repo (the real repo is never modified).
Agent A (Claude) hits a limit -> agent B (Claude-B or Kimi) takes over, finishes a task -> A resumes.
Checks: no history lost, nothing redone, lock transitions, inboxes respected, structure still valid."""
import hashlib, os, re, shutil, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_control import check

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ok = []


def step(name, cond, detail=""):
    ok.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (f" -- {detail}" if detail and not cond else ""))


def rd(p): return open(p, encoding="utf8").read()
def wr(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf8").write(s)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()


def handoff(agent, n, prev, done, inprog, nxt):
    return (f"# Handoff 2026-11-01-{n:02d} by {agent}\nPrevious handoff: [{prev}]({prev})\n## Done (with evidence)\n- {done}\n"
            f"## In progress (not finished)\n- {inprog}\n## Next action\n- {nxt}\n")


def main():
    tmp = tempfile.mkdtemp()
    repo = os.path.join(tmp, "repo")
    shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    arch = os.path.join(repo, "HANDOFFS", "archive")
    base = sorted(os.listdir(arch))
    base_hash = {n: sha(os.path.join(arch, n)) for n in base}
    step("0. baseline repo passes structure check", check(repo) == [], "; ".join(check(repo)))

    # Job inbox: one for the worker, one for Muse
    wr(os.path.join(repo, "JOBS/ACTIVE/TEST-0001.md"), "# TEST-0001\nStatus: ACTIVE\nAssignee: Claude\nTask: finish report part 1 and part 2.\n")
    wr(os.path.join(repo, "JOBS/PENDING/TEST-0002.md"), "# TEST-0002\nStatus: READY\nAssignee: Muse\nTask: apply patch (Muse only).\n")
    muse_before = sha(os.path.join(repo, "JOBS/PENDING/TEST-0002.md"))

    # 1. Claude finishes part 1, hits limit, writes handoff
    wr(os.path.join(repo, "TESTWORK/report.md"), "part 1 done by Claude\n")
    prev = base[-1]
    n1 = "2026-11-01-01-claude-limit.md"
    wr(os.path.join(arch, n1), handoff("Claude", 1, prev, "report part 1 (TESTWORK/report.md)", "part 2 not started", "write report part 2 (TEST-0001); Muse owns TEST-0002"))
    shutil.copy(os.path.join(arch, n1), os.path.join(repo, "HANDOFFS/LATEST.md"))
    wr(os.path.join(repo, "STATE/ACTIVE_WORKER.md"), "LOCK_STATUS: FREE\nLast driver: Claude\n")
    step("1. Claude handoff written, lock FREE, structure valid", check(repo) == [], "; ".join(check(repo)))

    # 2. Agent B reads LATEST, takes lock, identifies state, does only part 2
    latest = rd(os.path.join(repo, "HANDOFFS/LATEST.md"))
    done = re.search(r"## Done.*?\n- (.+)", latest, re.S).group(1)
    nxt = re.search(r"## Next action\n- (.+)", latest).group(1)
    step("2a. B identifies completed work", "part 1" in done)
    step("2b. B identifies exact next action", "part 2" in nxt and "TEST-0001" in nxt)
    wr(os.path.join(repo, "STATE/ACTIVE_WORKER.md"), "LOCK_STATUS: HELD\nJob: TEST-0001 Agent: Claude-B\n")
    report = rd(os.path.join(repo, "TESTWORK/report.md"))
    assignee = {f: re.search(r"Assignee:\s*(\S+)", rd(os.path.join(repo, "JOBS", d, f))).group(1)
                for d in ("ACTIVE", "PENDING") for f in os.listdir(os.path.join(repo, "JOBS", d)) if f.startswith("TEST-")}
    step("2c. B only works jobs assigned to it (not Muse's)", assignee["TEST-0002.md"] == "Muse")
    wr(os.path.join(repo, "TESTWORK/report.md"), report + "part 2 done by Claude-B\n")  # appends; does not redo part 1
    n2 = "2026-11-01-02-claudeb-done.md"
    wr(os.path.join(arch, n2), handoff("Claude-B", 2, n1, "report part 2 (TESTWORK/report.md)", "none", "Claude resumes; Muse applies patch (TEST-0002)"))
    shutil.copy(os.path.join(arch, n2), os.path.join(repo, "HANDOFFS/LATEST.md"))
    wr(os.path.join(repo, "STATE/ACTIVE_WORKER.md"), "LOCK_STATUS: FREE\nLast driver: Claude-B\n")
    step("2d. B handoff valid and links to A's handoff", check(repo) == [], "; ".join(check(repo)))

    # 3. Claude returns and resumes from B's handoff
    latest = rd(os.path.join(repo, "HANDOFFS/LATEST.md"))
    step("3a. A reads B's handoff as newest", "by Claude-B" in latest)
    step("3b. A sees part 1 and part 2 both done; nothing to redo", rd(os.path.join(repo, "TESTWORK/report.md")).count("part 1 done") == 1 and "part 2 done" in rd(os.path.join(repo, "TESTWORK/report.md")))
    step("3c. A knows remaining task is Muse's, not its own", "Muse applies patch" in latest)

    # 4. History intact; inbox untouched
    step("4a. no earlier handoff changed or deleted", all(os.path.exists(os.path.join(arch, n)) and sha(os.path.join(arch, n)) == h for n, h in base_hash.items()))
    step("4b. A's handoff preserved after B's", os.path.exists(os.path.join(arch, n1)))
    step("4c. Muse's inbox job unchanged", sha(os.path.join(repo, "JOBS/PENDING/TEST-0002.md")) == muse_before)
    step("4d. final structure check", check(repo) == [], "; ".join(check(repo)))
    shutil.rmtree(tmp)
    print(f"\n{sum(ok)}/{len(ok)} checks passed")
    return 0 if all(ok) else 1


if __name__ == "__main__":
    sys.exit(main())
