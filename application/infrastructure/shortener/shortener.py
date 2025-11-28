from secrets import token_urlsafe
from urllib.parse import urlparse

from application.ports import ShortenerPort


class Shortener(ShortenerPort):
    """
    Shorten a url.
    """

    def shorten(self, link: str) -> str:
        """
        Shorten a provided url.

        - Parse url, replace path and query params with a random sequence.

        Args:
            link (str): A url.
        
        Returns:
            str: A shortened version of the url that was provided.
        """
        scheme, netloc = urlparse(link)[:2]
        sequence = self.get_sequence()
        return self.compose_shortened_link(scheme=scheme, netloc=netloc, sequence=sequence)

    def get_sequence(self) -> str:
        """
        Get a random sequence.

        Returns:
            str: A 16 bytes string.
        """
        return token_urlsafe(16)
    
    def compose_shortened_link(self, scheme: str, netloc: str, sequence: str) -> str:
        """
        Compose the shortened link from the parsed url parts and a generated sequence.

        Args:
            scheme (str): A string that represents the link's scheme (http | https)
            netloc (str): A string that represents the link's domain (example.com)
            sequence (str): A string that represents a random sixteen bytes sequence.
        """
        return f'{scheme}://{netloc}/{sequence}'
