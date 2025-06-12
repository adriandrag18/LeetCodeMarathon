# LeetCode Marathon Script

This script retrieves your accepted LeetCode submissions, saves them to a Git repository, and commits them with backdated timestamps to reflect your solve dates. It uses a temporary branch for staging commits and merges them into the `main` branch.

## Prerequisites
- Python 3.x installed.
- Git installed and initialized in the `LeetCodeMarathon` directory.
- Environment variables set for authentication and Git configuration.

## Steps to Use

### 1. Obtain the Tokens
- **LeetCode Session Cookie and CSRF Token**:
  - Log in to LeetCode in your browser.
  - Open developer tools (F12), go to the "Network" tab, and refresh the page.
  - Find a request to `leetcode.com`, check the "Cookies" section, and copy:
    - `LEETCODE_SESSION` value.
    - `csrftoken` value.
  - Set these as environment variables:
    ```bash
    export LEETCODE_SESSION="your_leetcode_session"
    export CSRF_TOKEN="your_csrf_token"
    ```
- **Git Email and Username**:
  - Use a GitHub-associated email (e.g., `66696874+adrianandrag18@users.noreply.github.com`) and your GitHub username (e.g., `adrianandrag18`).
  - Set these as environment variables:
    ```bash
    export GIT_EMAIL="your_email"
    export GIT_USERNAME="your_username"
    ```
  - Alternatively, the script will prompt for these if not set.

### 2. Install Requirements
- Install the required Python package using pip:
  ```bash
  pip install -r requirements.txt
  ```
  - Ensure you use a virtual environment (e.g., `python3 -m venv venv` and `source venv/bin/activate`) to avoid system conflicts.

### 3. Run the Script
- Navigate to the `LeetCodeMarathon` directory (where the script and `.git` are).
- Run the script:
  ```bash
  python soulutionRetriver.py
  ```
- The script will:
  - Fetch your last accepted LeetCode submissions in batches of 20 (with a 2-second delay).
  - Save them to the `Problems` folder.
  - Commit each new file to a temporary branch (`backdated-solutions`) with the original solve date.
  - Merge into `main` and clean up the temp branch.
- To push to a remote repository (e.g., GitHub), uncomment the push line in the script and run:
  ```bash
  git push origin main --force
  ```
  - Use `--force` with caution as it overwrites remote history.

## Notes
- **Offset**: The `startOffset` is set to 0. Adjust if resuming a failed run.
- **Existing Files**: Skips files already saved or committed.
- **Backdating**: Commits are backdated to the submission timestamp for accurate GitHub contributions.
- **Environment**: Ensure all environment variables are set, or be prepared to enter them when prompted.

## Troubleshooting
- If tokens expire, re-obtain them from LeetCode.
- Check Git status with `git status` if commits fail.
- Use `git log -- Problems` to see committed files in the `Problems` folder.

Happy coding and contributing to your LeetCode marathon!