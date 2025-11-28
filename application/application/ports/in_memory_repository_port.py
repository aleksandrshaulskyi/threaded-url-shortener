from abc import ABC, abstractmethod


class InMemoryRepositoryPort(ABC):
    """
    This abstraction is used to define the main methods that are used to
    store and retrieve full link to and from the in-memory repository.
    """

    @abstractmethod
    def store(self, shortened_link_data: dict) -> None:
        """
        This method should provide functionality that would allow storing
        a k: v pair of shortened link and full link to the in memory storage.
        """
        ...

    @abstractmethod
    def retrieve(self, shortened_link: str) -> str:
        """
        As the method name suggests this abstraction should provide functionality
        to retrieve the full link by it's shortened counterpart.
        """
        ...
