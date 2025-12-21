import nox

@nox.session
def tests(session) -> None:
    session.install('pytest')
    """
        run tests suite
    """
    session.run('pytest')