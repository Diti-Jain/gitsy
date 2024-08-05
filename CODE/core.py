import os



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
        if branch != None:
            self.change_branch(branch)
        stream = os.popen('git push origin head')
        stream.read()

    def change_branch(self,branch):
        try:
            stream = os.popen('git checkout ' + branch)
            stream.read()
        except:
            stream = os.popen('git checkout -b '+ branch)
            stream.read()