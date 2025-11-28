from concurrent.futures import Future


def shortening_callback(future: Future | None) -> None:
    """
    A callback to avoid blocking the thread as it is fancier to print it here
    than in the runner.

    Or S from SOLID.
    """
    if (link := future.result()) is not None:
        print(f'The link is: {link}')
