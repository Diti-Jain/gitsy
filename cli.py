import argparse
from CODE.core import GitsyCommand
import os
import time

def main():
    parser = argparse.ArgumentParser(description="Gitsy: A simple tool for git cli")
    subparsers = parser.add_subparsers(dest='command',help="Subcommands")

    push_parser=subparsers.add_parser('push',help='Push changes to a branch')
    push_parser.add_argument('-m','--message',default=None,  help='The commit message')
    push_parser.add_argument('-b','--branch',default= None ,  help='The branch to push to')
    push_parser.add_argument('-t','--time',default=time.strftime("%H:%M", time.localtime()), help='The time you want to push your commit')
    push_parser.add_argument('-f','--file',nargs='+' ,default=None, help='Specific file name to push')
    push_parser.add_argument('-na',action='store_true',help='To avoid the add stage')
    #for demonstration

    pull_parser=subparsers.add_parser('pull',help='pulls from the branch')

    origin_parser=subparsers.add_parser('init',help='To add a github repo to a folder')
    origin_parser.add_argument('-u','--url',default=None,help="Add the url to repo")

    args = parser.parse_args()
    execute_command(args)

def execute_command(args):
    gs = GitsyCommand(os.getcwd())
    command = args.command
    if command == 'push':
        message=args.message if args.message else None
        file=args.file if args.file else None
        time=args.time if args.time else time.strftime("%H:%M", time.localtime())
        branch = args.branch if args.branch else None
        gs.push(message,branch,time,file,args.na)
        print("successful")
    elif command == 'pull':
        gs.pull()
    elif command == 'init':
        url=args.url if args.url else None
        gs.add_origin(url)
    #for demonstration 
        


if __name__ == "__main__":
    main()
