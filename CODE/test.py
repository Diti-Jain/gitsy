import subprocess
import sys
result = subprocess.run(["git", "diff", "--cached", "--quiet"], check=True)
if result.returncode == 0:
    print("No changes staged for commit.")
    sys.exit(0)

git diff --name-only --cached