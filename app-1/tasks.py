from invoke import task
from time import sleep
from subprocess import run



"""
    help functions for help in development
    git
    lint
    blue
    isort

    run in terminal:
    # poetry run invoke tests
    # invoke git
    # python invoke git
"""

@task
def git(context: str = '') -> None:
    """
        sync repo
    """
    run(['git', 'pull'])
    run(['git', 'push'])
    run(['git', 'fetch', '--all'])

@task
def lint(context: str = '') -> None:
    # run(["blue", "--check", "--diff", "."]) 
    run(['isort', '.']) 