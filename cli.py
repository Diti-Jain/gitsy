
import argparse
from CODE.core import GitsyCommand
import os

def main():


    parser = argparse.ArgumentParser(description="Gitsy: A simple tool for git cli")
    subparsers = parser.add_subparsers(dest='command',help="Subcommands")


    push_parser=subparsers.add_parser('push',help='Push changes to a branch')
    push_parser.add_argument('message', help='The commit message')
    push_parser.add_argument('-b','--branch',default= None ,  help='The branch to push to')


    args = parser.parse_args()
    execute_command(args)

def execute_command(args):
    gs = GitsyCommand(os.getcwd())
    command = args.command

    if command == 'push':
        branch = args.branch if args.branch else None
        gs.push(args.message,branch)
        print("successful")





if __name__ == "__main__":
    main()
