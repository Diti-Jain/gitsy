import argparse
from CODE.core import GitsyCommand
import os
import time

def main():
    parser = argparse.ArgumentParser(description="Gitsy: A simple tool for git cli")
    subparsers = parser.add_subparsers(dest='command',help="Subcommands")

    push_parser=subparsers.add_parser('push',help='Push changes to a branch')
    push_parser.add_argument('message', help='The commit message')

    push_parser.add_argument('-b','--branch',default= None ,  help='The branch to push to')
    push_parser.add_argument('-t','--time',default=time.strftime("%H:%M", time.localtime()), help='The time you want to push your commit')
    push_parser.add_argument('-f','--file',nargs='+' ,default='.', help='Specific file name to push')
    args = parser.parse_args()
    execute_command(args)

def execute_command(args):
    gs = GitsyCommand(os.getcwd())
    command = args.command
    if command == 'push':
        file=args.file if args.file else '.'
        time=args.time if args.time else time.strftime("%H:%M", time.localtime())
        branch = args.branch if args.branch else None
        gs.push(args.message,branch,time,file)
        print("successful")

if __name__ == "__main__":
    main()
