import os
try:
    try:

        stream = os.popen('git checkout -b newbranch')
        stream.read()
    except:
        stream = os.popen('git checkout newbranch')
        stream.read()


    stream = os.popen('git add .')
    stream.read()

    stream = os.popen(r'git commit -m "newbranch testing "')
    stream.read()

    stream = os.popen('git push origin head')
    stream.read()
except:
    text="GitHub not authenticated"
    cmd = "echo {} ".format(text)
    os.syetem(cmd)
