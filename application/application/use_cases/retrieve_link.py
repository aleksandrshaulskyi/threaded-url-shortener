from application.exceptions import LinkNotFoundException
from application.ports import InMemoryRepositoryPort

from infrastructure.repository import in_memory_repository


class RetrieveLinkUseCase:
    """
    This use case retrieves the full link by it's shortened counterpart for the in-memory storage.
    """
    
    def __init__(self, link: str, repo: InMemoryRepositoryPort) -> None:
        """
        Initialize the use case.

        Args:
            link (str): A previously shortened link.
            repo (InMemoryRepositoryPort): The port that is used for storing shortened links in memory.
        """
        self.link = link
        self.repo = repo

    def execute(self) -> str | None:
        """
        Execute the process.

        Returns:
            str: A string if a full link was found and None otherwise.

        Raises:
            LinkNotFoundException: If a full link was not found by the provided shortened version.
        """
        if (link := self.repo.retrieve(shortened_link=self.link)) is None:
            raise LinkNotFoundException(
                title='Link was not found.',
                details={'Link was not found.': 'Could not found the full link by the link you have provided.'},
            )
        return link
