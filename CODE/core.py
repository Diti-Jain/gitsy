import subprocess
import time
import os

class GitsyCommand:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def automessage(self):
        result=subprocess.run(['git','status','--porcelain'],stdout=subprocess.PIPE, stderr=subprocess.PIPE,text=True)
        git_status_output=result.stdout.strip()
        if not git_status_output:
            return 'no changes to commit'
        added = []
        modified = []
        deleted = []
        renamed = []
        untracked = []
        others = []

        for line in git_status_output.splitlines():
            arr=line.split()
            status=arr[0]
            file_name=arr[1]
            if status == 'A':
                added.append(file_name)
            elif status in ['M', 'MM']:
                modified.append(file_name)
            elif status == 'D':
                deleted.append(file_name)
            elif status == 'R':
                renamed.append(file_name)
            elif status == '??':
                untracked.append(file_name)
            else:
                others.append(f"{status}: {file_name}")

        commit_message_parts = []
        if added:
            commit_message_parts.append(f"Added: {', '.join(added)}")
        if modified:
            commit_message_parts.append(f"Modified: {', '.join(modified)}")
        if deleted:
            commit_message_parts.append(f"Deleted: {', '.join(deleted)}")
        if renamed:
            commit_message_parts.append(f"Renamed: {', '.join(renamed)}")
        if untracked:
            commit_message_parts.append(f"Untracked: {', '.join(untracked)}")
        if others:
            commit_message_parts.append(f"Other changes: {', '.join(others)}")
        return "; ".join(commit_message_parts)

    def add(self,file):
        if file==None:
            subprocess.run(['git','add','.'],check=True)
        else:
            subprocess.run(["git", "add"]+ file, check=True)

    def commit(self, message):
        if message==None:
            message=self.automessage()
        subprocess.run(["git", "commit", "-m", message], check=True)

    def push(self, message, branch, time1,file,na):
        if not na:
            self.add(file)
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