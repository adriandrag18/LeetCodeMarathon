import requests
import os
import time
import subprocess
from datetime import datetime

# Configuration
leetcodeSession = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI0NjY0NDciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVhODkyOGZlMDQ2MDI4NzA4NTM4YzQzMDIzMzljMTE5NzE1MGE4MzM3N2I4MmQ5YmNlZDA4NDRiMTM2MTA0ZTIiLCJzZXNzaW9uX3V1aWQiOiIxZjg2NDU0NCIsImlkIjoxMjQ2NjQ0NywiZW1haWwiOiJhZHJpYW5kcmFnMTk5MkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6ImFkcmlhbmRyYWcxOCIsInVzZXJfc2x1ZyI6ImFkcmlhbmRyYWcxOCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9kZWZhdWx0X2F2YXRhci5qcGciLCJyZWZyZXNoZWRfYXQiOjE3NDk2MjIyNzUsImlwIjoiMmEwMjoyZjAwOjQwYTo5ZjAwOmM4ODM6ZjJlOToxNWM0OjM0NGIiLCJpZGVudGl0eSI6IjllYTg2Y2M4ZmRkYTI4OTViOWUzOGI5YWI1MGM5YzY2IiwiZGV2aWNlX3dpdGhfaXAiOlsiZTk4OTgyNGMzMjcyMWUyNDYzMDIxMmVlNmE4NWY4OGQiLCIyYTAyOjJmMDA6NDBhOjlmMDA6Yzg4MzpmMmU5OjE1YzQ6MzQ0YiJdLCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.piNGSjubiiXut0EeYKGboM4sMgz1foGn6Fa04fmbTRw"
csrfToken = "37onagxj7WPS0vDc9PjRqgNFTVNzqAnmNeL2uTHdQGKo91FZrHqupQbxIxbUF1hx"
BASE_URL = "https://leetcode.com"
problemsDir = "Problems"
BATCH_SIZE = 20
SLEEP_TIME = 2
startOffset = 0
LIMIT = 2000
EMAIL = "66696874+adrianandrag18@users.noreply.github.com"
USERNAME = "adrianandrag18"
extMap = {"python3": ".py", "cpp": ".cpp", "go": ".go"}

def getAcceptedSubmissions():
    headers = {
        "Cookie": f"LEETCODE_SESSION={leetcodeSession}; csrftoken={csrfToken}",
        "X-CSRFToken": csrfToken,
        "Referer": f"{BASE_URL}/submissions/",
        "User-Agent": "Mozilla/5.0"
    }
    offset = startOffset
    
    while offset < LIMIT:
        url = f"{BASE_URL}/api/submissions/?offset={offset}&limit={BATCH_SIZE}&lastkey="
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed at offset {offset}: {response.status_code} {response.reason}")
            break
        data = response.json()
        submissions = [s for s in data["submissions_dump"] if s["status_display"] == "Accepted"][:LIMIT]
        for submission in submissions:
            yield submission
        if not data.get("has_next"):
            print('No more data')
            break
        offset += len(submissions)
        time.sleep(SLEEP_TIME)

def getLanguageCommentStyle(lang):
    commentStyles = {"python3": "#", "cpp": "//", "golang": "//"}
    return commentStyles.get(lang, "#")

def saveSubmissionToFile(submission):
    questionId = submission["question_id"]
    titleSlug = submission["title_slug"]
    lang = submission["lang"]
    timestamp = datetime.fromtimestamp(submission["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
    code = submission["code"]
    ext = extMap.get(lang, ".txt")
    filename = f"{questionId}.{titleSlug}{ext}"
    filepath = os.path.join(problemsDir, filename)

    if os.path.exists(filepath):
        print(f"Skipping {filename}: File already exists")
        return filepath

    commentStyle = getLanguageCommentStyle(lang)
    metadataLines = [
        f"{commentStyle} title: {submission['title']}",
        f"{commentStyle} timestamp: {timestamp}",
        f"{commentStyle} problemUrl: {BASE_URL}/problems/{titleSlug}/",
        f"{commentStyle} memory: {submission['memory']}",
        f"{commentStyle} runtime: {submission['runtime']}"
    ]
    metadataBlock = "\n".join(metadataLines)

    content = f"{metadataBlock}\n\n{code}"
    os.makedirs(problemsDir, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {filename}")
    return filepath

def isFileCommitted(filepath):
    try:
        # result = subprocess.run(["git", "ls-files", filepath], capture_output=True, text=True)
        # print(filepath, result)
        # if result.stdout != 0 or result.stdout:  # File not tracked
        #     return False
        # Check commit history for the file
        result = subprocess.run(["git", "log", "--oneline", filepath], capture_output=True, text=True)
        print(2, filepath, result)
        return result.returncode == 0 and result.stdout
    except subprocess.CalledProcessError:
        return False

def commitSolution(filepath, timestamp):
    if isFileCommitted(filepath):
        print(f"Skipping commit for {os.path.basename(filepath)}: Already committed")
        return
    dateStr = timestamp
    subprocess.run(["git", "add", filepath], check=True)
    print('git add', filepath)
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = dateStr
    env["GIT_AUTHOR_DATE"] = dateStr
    subprocess.run(["git", "commit", "-m", f"Add solution for {os.path.basename(filepath)}"], env=env, check=True)

def main():
    subprocess.run(["git", "config", "user.name", USERNAME], check=True)
    subprocess.run(["git", "config", "user.email", EMAIL], check=True)
    tempBranch = "solutions"
    subprocess.run(["git", "add", "soulutionRetriver.py"], check=True)
    subprocess.run(["git", "commit", "--amend", "--no-edit"], check=True)
    try:
        subprocess.run(["git", "checkout", "--orphan", tempBranch], check=True)
    except:
        subprocess.run(["git", "branch", "-D", tempBranch], check=True)
        subprocess.run(["git", "checkout", "--orphan", tempBranch], check=True)
    
    totalSubmissions = 0
    for submission in getAcceptedSubmissions():
        filepath = saveSubmissionToFile(submission)
        timestamp = datetime.fromtimestamp(submission["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        commitSolution(filepath, timestamp)
        totalSubmissions += 1

    subprocess.run(["git", "checkout", "main"], check=True)

    try:
        subprocess.run(["git", "merge", "--no-ff", "--allow-unrelated-histories", tempBranch], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Warning: Merge failed with error: {e}. Attempting force merge.")
        subprocess.run(["git", "merge", "--allow-unrelated-histories", tempBranch], check=True)
    # subprocess.run(["git", "branch", "-D", tempBranch], check=True)

    # Push to remote (uncomment to enable)
    # subprocess.run(["git", "push", "origin", "main", "--force"], check=True)

    print(f"Finished saving and committing {totalSubmissions} solutions to LeetCodeMarathon")

if __name__ == "__main__":
    main()