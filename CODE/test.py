import os
stream = os.popen('git add .')
stream.read()

stream = os.popen(r'git commit -m "initial test" ')
stream.read()

stream = os.popen('git push origin main')
stream.read()
