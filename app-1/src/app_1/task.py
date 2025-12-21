from invoke import task
from time import sleep

@task
def sync(context: str) -> None:
    """
        git repo sync
        - git pull
        - git push
    """
    print('building')
    sleep(2)
    print('building')
