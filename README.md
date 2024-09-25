# Gitsy: Git CLI made easy

**Gitsy** is a command-line tool designed to streamline Git workflows by reducing the complexity of common Git commands into simpler, more intuitive actions. With Gitsy, developers can push, pull, and manage Git repositories with fewer steps, making version control more efficient.

## Features

- **Simplified Git push:** Combine `git add`, `git commit`, and `git push` into one command.
- **Automatic Commit Messages:** If no message is provided, Gitsy auto-generates a commit message.
- **Branch Creation on the Fly:** Push to a new branch automatically if it doesn’t exist.
- **Scheduled Pushes:** Set a time to push changes.
- **File-Specific Push:** Add and push only specific files with ease.
- **Streamlined Pull:** Pull changes from a branch using a single command.
- **Repository Initialization:** Easily initialize a local folder with a remote repository.

## Installation

Clone the repository:

```shell
git clone https://github.com/diti-jain/gitsy
cd gitsy
```

Install the package:

```shell
pip install -e .
```

## Usage

### Initialize a repository:

```shell
gitsy init
```

This will initialize the current directory as a Git repository.

### Push changes

```shell
gitsy push
```

This command combines `git add .`, `git commit -m "Commit Message"`, and `git push` into one. You can also use the following options:

- **-m**: Specify a commit message

```shell
gitsy push -m "Commit message"
```

If no message is provided, Gitsy will auto-generate a commit message.

- **-b**: Push to a specific branch, creating the branch if it doesn’t exist.

```shell
gitsy push -b feature-branch
```

If no branch is provided, Gitsy will push the commit to the current working branch.

- **-t**: Schedule your push for a specific time.

```shell
gitsy push -t "14:00"
```

If no time is provided, Gitsy will push the commit at the current time.

- **-f**: Push specific files.

```shell
gitsy push -f file1.txt file2.txt

```

If no files are provided, Gitsy will push the commit with adding all the files.

### Pull changes

```shell
gitsy pull
```

Fetch and pull changes from the specified branch.

### View Help

```shell
gitsy --help
```

Get detailed information on Gitsy's commands and options.

## Project Structure

```

gitsy/
├── CODE/
│ ├── __init__.py
│ └── core.py
├── cli.py
├── setup.py
└── README.md

```

## Future Versions

- Support for additional Git commands.
- Improved error handling and logging.
- Integration with GitHub and GitLab APIs for managing repositories directly from Gitsy.

## Contributing

Gitsy is a collaborative project by [**Diti Jain**](https://github.com/Diti-Jain) and [**Dev Mehta**](https://github.com/DevMehta-30). Together, we aim to streamline Git workflows for developers.

While this is a joint effort, we’re always open to feedback, suggestions, and contributions from the community. Feel free to open an issue or submit a pull request. Let’s improve Gitsy together!

## References

1. [Git Documentation](https://git-scm.com/doc)
2. [GitHub CLI Documentation](https://cli.github.com/manual/)
