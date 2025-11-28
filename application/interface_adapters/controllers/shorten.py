from application.ports import InMemoryRepositoryPort, ShortenerPort
from application.use_cases import ShortenUrlUseCase
from interface_adapters.outgoing_dtos import OutgoingLinkDTO


class ShortenUrlController:
    """
    This controller is responsible for the incapsulation of the business
    logic and adaption of the data that is returned from the use case.
    """

    def __init__(self, link: str, repo: InMemoryRepositoryPort, shortener: ShortenerPort) -> None:
        """
        Initialize the controller.

        Args:
            link (str): A link that need to be shortened.
            repo (InMemoryRepositoryPort): The abstraction (port) that is used for operations in the in-memory storage.
            shortener (ShortenerPort) The abstraction (port) that is used to shorten a link.
        """
        self.link = link
        self.repo = repo
        self.shortener = shortener

    def shorten(self) -> dict:
        """
        Shorten a link.

        - Call the respectful use case.
        - Adapt the outgoing data.
        """
        use_case = ShortenUrlUseCase(link=self.link, repo=self.repo, shortener=self.shortener)

        shortened_link_data = use_case.execute()

        return OutgoingLinkDTO.create(data=shortened_link_data).representation
        