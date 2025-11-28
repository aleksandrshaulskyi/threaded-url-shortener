from dataclasses import dataclass


@dataclass
class OutgoingLinkDTO:
    """
    The dataclass that is used to return an instance of ShortLink entity
    in the format that is acceptable for the outside world.
    """
    link: str

    @property
    def representation(self) -> str:
        return self.link

    @classmethod
    def create(cls, data: dict) -> 'OutgoingLinkDTO':
        """
        Safely create an instance of the OutgoingLinkDTO dataclass.
        """
        return OutgoingLinkDTO(link=data.get('shortened'))
