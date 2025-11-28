from abc import ABC, abstractmethod


class ShortenerPort(ABC):
    """
    Shorten the provided link.
    """

    @abstractmethod
    def shorten(self, link: str) -> str:
        """
        This abstraction should allow us to receive a shortened link.
        """
        ...
