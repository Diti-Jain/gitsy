import subprocess
import time
import os

class GitsyCommand:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def add(self):
        subprocess.run(["git", "add", "."], check=True)

    def commit(self, message):
        subprocess.run(["git", "commit", "-m", message], check=True)

    def push(self, message, branch, time1):
        self.add()
        self.commit(message)

        while True:
            current_time = time.strftime("%H:%M", time.localtime())
            if current_time >= time1:
                break
            time.sleep(30)

        print(f"Current time ({current_time}) is now greater than or equal to the scheduled time ({time1}).")

        if branch:
            try:
                print(f"Attempting to push to branch: {branch}")
                subprocess.run(["git", "push", "origin", branch], check=True)
                print("Push to specified branch successful (HI2).")
            except subprocess.CalledProcessError:
                try:
                    print(f"Push failed. Trying to create and checkout new branch: {branch}")
                    subprocess.run(["git", "checkout", "-b", branch], check=True)
                    subprocess.run(["git", "push", "-f", "origin", branch], check=True)
                    print("Branch creation and force push successful (HI3).")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to push to or create branch '{branch}': {e}")
        else:
            print("No branch specified. Pushing to 'HEAD'.")
            stream = os.popen('git push origin HEAD')
            output = stream.read()
            print(output)



