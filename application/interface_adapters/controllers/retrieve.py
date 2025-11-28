from application.ports import InMemoryRepositoryPort
from application.use_cases import RetrieveLinkUseCase
from interface_adapters.outgoing_dtos import OutgoingLinkDTO


class RetriveUrlController:
    """"
    This controller is responsible for the retrieval of a full link by it's shortened counterpart.
    """

    def __init__(self, link: str, repo: InMemoryRepositoryPort) -> None:
        """
        Initialize the controller.

        Args:
            link (str): A previously shortened link.
            repo (InMemoryRepositoryPort): The port that is used for storing shortened links in memory.
        """
        self.link = link
        self.repo = repo

    def retrieve_link(self) -> str:
        """
        Retrieve a full link.
        """
        use_case = RetrieveLinkUseCase(link=self.link, repo=self.repo)

        return OutgoingLinkDTO(link=use_case.execute()).representation
