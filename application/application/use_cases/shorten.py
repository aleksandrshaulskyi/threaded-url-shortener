from application.ports import InMemoryRepositoryPort, ShortenerPort
from domain.entities import ShortLink


class ShortenUrlUseCase:
    """
    This use case is used to shorten a url.
    """

    def __init__(self, link: str, repo: InMemoryRepositoryPort, shortener: ShortenerPort) -> None:
        """
        Initialize the use case.

        Args:
            link (str): A link.
            repo (InMemoryRepositoryPort): The abstraction (port) that is used for operations in the in-memory storage.
            shortener (ShortenerPort) The abstraction (port) that is used to shorten a link.
        """
        self.link = link
        self.repo = repo
        self.shortener = shortener

    def execute(self) -> str:
        """
        Execute the process.

        - Get a random sequence.
        - Store it into the storage.
        """
        shortened_link = self.shortener.shorten(link=self.link)

        shortened_link_data = ShortLink.create({'original': self.link, 'shortened': shortened_link})

        self.repo.store(shortened_link_data=shortened_link_data.representation)

        return shortened_link_data.representation
