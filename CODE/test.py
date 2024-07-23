import os
try:
    stream = os.popen('git add .')
    stream.read()

    stream = os.popen(r'git commit -m "checking for git auth"')
    stream.read()

    stream = os.popen('git push origin main')
    stream.read()
except:
    text="GitHub not authenticated"
    cmd = "echo {} ".format(text)
    os.syetem(cmd)
