from dataclasses import asdict, dataclass


@dataclass
class ShortLink:
    """
    The main domain entity.
    """
    original: str
    shortened: str

    @property
    def representation(self) -> dict:
        """
        Get an instance of ShortLink as a dictionary.
        """
        return asdict(self)

    @classmethod
    def create(self, data: dict) -> 'ShortLink':
        """
        Safely create an instance of the ShortLink entity.
        """
        return ShortLink(
            original=data.get('original'),
            shortened=data.get('shortened'),
        )
