#!/usr/bin/env python3
"""
Helper script to add/update a quiz generated in Antigravity into quizzes-library.json,
pulling any quizzes already uploaded to GitHub from mobile/web devices so all quizzes
stay unified and accessible on every device.
"""
import json
import os
import sys
import subprocess
from datetime import datetime, timezone

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_PATH = os.path.join(REPO_DIR, "quizzes-library.json")


def sync_and_publish(new_quiz_path=None):
    os.chdir(REPO_DIR)
    subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)

    if os.path.exists(LIB_PATH):
        with open(LIB_PATH, "r", encoding="utf-8") as f:
            lib = json.load(f)
    else:
        lib = {"activeQuizId": "default_ch1", "updatedAt": "", "quizzes": []}

    if new_quiz_path and os.path.exists(new_quiz_path):
        with open(new_quiz_path, "r", encoding="utf-8") as f:
            new_q = json.load(f)
        qid = new_q.get("id") or f"quiz_{int(datetime.now().timestamp())}"
        new_q["id"] = qid
        lib["quizzes"] = [q for q in lib.get("quizzes", []) if q.get("id") != qid]
        lib["quizzes"].insert(0, new_q)
        lib["activeQuizId"] = qid

    lib["updatedAt"] = datetime.now(timezone.utc).isoformat()
    with open(LIB_PATH, "w", encoding="utf-8") as f:
        json.dump(lib, f, indent=2, ensure_ascii=False)

    subprocess.run(["git", "add", "quizzes-library.json"], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Publish quiz to GitHub library (active: {lib.get('activeQuizId')})"],
        check=False,
    )
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print(f"Successfully synced {len(lib.get('quizzes', []))} custom quizzes to GitHub!")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    sync_and_publish(arg)
