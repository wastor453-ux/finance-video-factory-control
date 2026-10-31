#!/usr/bin/env python3
"""Structure checks for this repo (stdlib only). Usage: python3 tools/check_repo.py [repo_root]
Checks: required files, STATUS lock line, LATEST == newest handoff, 'Previous handoff' links resolve, job files have
Status, LOG.md is append-only-looking (entries in order), no obvious secrets. Exit 1 on any problem."""
import os, re, sys

REQUIRED = ["README.md", "START_HERE.md", "PROJECT_BIBLE.md", "STATUS.md", "LOG.md", "DECISIONS.md", "PATCHES.md", "MUSE_PLAYBOOK.md", "CLAUDE.md"]
SECRET = re.compile(r"AIza[0-9A-Za-z_-]{20,}|ghp_[0-9A-Za-z]{20,}|github_pat_[0-9A-Za-z_]{20,}|sk-[0-9A-Za-z]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----")


def rd(p):
    with open(p, encoding="utf8") as f:
        return f.read()


def check(root):
    p = []
    j = lambda *a: os.path.join(root, *a)
    for r in REQUIRED:
        if not os.path.exists(j(r)):
            p.append(f"{r} missing")
    if os.path.exists(j("STATUS.md")) and not re.search(r"^LOCK:\s*(FREE|HELD)", rd(j("STATUS.md")), re.M):
        p.append("STATUS.md: no 'LOCK: FREE' or 'LOCK: HELD ...' line")
    hd = j("HANDOFFS")
    names = sorted(n for n in os.listdir(hd) if n.endswith(".md") and n != "LATEST.md") if os.path.isdir(hd) else []
    if not names:
        p.append("HANDOFFS has no dated handoff")
    else:
        if not os.path.exists(j("HANDOFFS", "LATEST.md")):
            p.append("HANDOFFS/LATEST.md missing")
        elif rd(j("HANDOFFS", "LATEST.md")) != rd(j("HANDOFFS", names[-1])):
            p.append(f"HANDOFFS/LATEST.md is not identical to the newest handoff ({names[-1]})")
        for i, n in enumerate(names):
            m = re.search(r"^Previous handoff:\s*(.+)$", rd(j("HANDOFFS", n)), re.M)
            if m:
                link = re.search(r"\(([^)]+\.md)\)", m.group(1))
                if link and not os.path.exists(j("HANDOFFS", link.group(1))):
                    p.append(f"{n}: previous handoff link does not resolve")
            elif i > 0:
                p.append(f"{n}: missing 'Previous handoff:' link")
    for d in ("todo", "doing", "done"):
        dd = j("JOBS", d)
        if not os.path.isdir(dd):
            p.append(f"JOBS/{d} missing")
            continue
        for n in sorted(os.listdir(dd)):
            if n.endswith(".md") and not re.search(r"Status:", rd(os.path.join(dd, n))):
                p.append(f"JOBS/{d}/{n}: no 'Status:' line")
    if os.path.exists(j("LOG.md")):
        ids = re.findall(r"^## (\d{4}-\d{2}-\d{2})-(\d+) \|", rd(j("LOG.md")), re.M)
        if ids != sorted(ids):
            p.append("LOG.md entries are not in date order (append at the bottom)")
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f.endswith((".md", ".py", ".json", ".txt")) and SECRET.search(open(os.path.join(dirpath, f), encoding="utf8", errors="ignore").read()):
                p.append(f"possible secret in {os.path.relpath(os.path.join(dirpath, f), root)}")
    return p


if __name__ == "__main__":
    probs = check(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    print("REPO OK" if not probs else "\n".join(probs))
    sys.exit(1 if probs else 0)
