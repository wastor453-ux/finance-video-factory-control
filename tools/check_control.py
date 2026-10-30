#!/usr/bin/env python3
"""Structure checks for the control repo (stdlib only). Usage: python3 tools/check_control.py [repo_root]
Checks: lock status line, LATEST == newest archived handoff, handoff 'Previous handoff' links resolve, job files
carry a Status, no obvious secrets. Exit 1 on any problem."""
import os, re, sys

SECRET = re.compile(r"AIza[0-9A-Za-z_-]{20,}|ghp_[0-9A-Za-z]{20,}|github_pat_[0-9A-Za-z_]{20,}|sk-[0-9A-Za-z]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----")


def check(root):
    p = []
    j = lambda *a: os.path.join(root, *a)
    try:
        lock = open(j("STATE", "ACTIVE_WORKER.md"), encoding="utf8").read()
        if not re.search(r"LOCK_STATUS:\s*(FREE|HELD)", lock):
            p.append("STATE/ACTIVE_WORKER.md: no 'LOCK_STATUS: FREE|HELD' line")
    except FileNotFoundError:
        p.append("STATE/ACTIVE_WORKER.md missing")
    arch = j("HANDOFFS", "archive")
    names = sorted(n for n in os.listdir(arch) if n.endswith(".md")) if os.path.isdir(arch) else []
    if not names:
        p.append("HANDOFFS/archive has no handoffs")
    else:
        latest = j("HANDOFFS", "LATEST.md")
        if not os.path.exists(latest):
            p.append("HANDOFFS/LATEST.md missing")
        elif open(latest, encoding="utf8").read() != open(os.path.join(arch, names[-1]), encoding="utf8").read():
            p.append(f"HANDOFFS/LATEST.md is not identical to the newest archived handoff ({names[-1]})")
        for i, n in enumerate(names):
            txt = open(os.path.join(arch, n), encoding="utf8").read()
            m = re.search(r"^Previous handoff:\s*(.+)$", txt, re.M)
            if i > 0:
                if not m:
                    p.append(f"{n}: missing 'Previous handoff:' link")
                else:
                    link = re.search(r"\(([^)]+\.md)\)", m.group(1))
                    if link and not os.path.exists(os.path.join(arch, link.group(1))):
                        p.append(f"{n}: previous handoff link does not resolve")
    for d in ("ACTIVE", "PENDING", "DONE"):
        dd = j("JOBS", d)
        for n in sorted(os.listdir(dd)) if os.path.isdir(dd) else []:
            if n.endswith(".md") and not re.search(r"Status:", open(os.path.join(dd, n), encoding="utf8").read()):
                p.append(f"JOBS/{d}/{n}: no 'Status:' line")
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            if f.endswith((".md", ".py", ".json", ".txt")):
                if SECRET.search(open(os.path.join(dirpath, f), encoding="utf8", errors="ignore").read()):
                    p.append(f"possible secret in {os.path.relpath(os.path.join(dirpath, f), root)}")
    return p


if __name__ == "__main__":
    probs = check(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    print("CONTROL OK" if not probs else "\n".join(probs))
    sys.exit(1 if probs else 0)
