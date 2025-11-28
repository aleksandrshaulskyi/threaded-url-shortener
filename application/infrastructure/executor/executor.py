from concurrent.futures import ThreadPoolExecutor


class Executor:
    """
    The wrapper of the ThreadPoolExecutor.
    """

    def __init__(self) -> None:
        """
        Initialize the executor.
        """
        self.executor = ThreadPoolExecutor(max_workers=8)

    def stop(self) -> None:
        """
        Shutfown the executor.
        """
        self.executor.shutdown(wait=True)

executor = Executor()
