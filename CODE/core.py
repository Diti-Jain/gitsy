import os
import subprocess
class GitsyCommand:
    def __init__(self, root_dir):
        self.root_dir = os.path.abspath(root_dir)
        self.code_dir = os.path.join(self.root_dir, '.code')
        self.objects_dir = os.path.join(self.code_dir, 'objects')
        self.refs_dir = os.path.join(self.code_dir, 'refs')

    def add(self):
        stream = os.popen('git add .')
        stream.read()
    def commit(self,message):
        stream = os.popen(r'git commit -m "'+ message + '"')
        stream.read()
    def push(self, message,branch):
        self.add()
        self.commit(message)
        if branch:
            try:
                # Attempt to push to the specified branch
                subprocess.run(["git", "push", "origin", branch], check=True)
                print("HI2")
            except subprocess.CalledProcessError:
                try:
                    # If push fails, try creating and checking out a new branch
                    subprocess.run(["git", "checkout", "-b", branch], check=True)
                    subprocess.run(["git", "push", "-f", "origin", branch], check=True)
                    print("HI3")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to push to or create branch '{branch}': {e}")
        else:
            stream = os.popen('git push origin head')
            stream.read()

