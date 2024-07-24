
import argparse
from CODE.core import GitsyCommand
import os

def main():


    parser = argparse.ArgumentParser(description="Gitsy: A simple tool for git cli")
    subparsers = parser.add_subparsers(dest='command')


    subparsers.add_parser('push').add_argument('message')


    args = parser.parse_args()
    execute_command(args)

def execute_command(args):
    gs = GitsyCommand(os.getcwd())
    command = args.command

    if command == 'push':
        push_id= gs.push(args.message)
        print("successful"+ push_id)





if __name__ == "__main__":
    main()
