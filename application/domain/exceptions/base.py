class BaseException(Exception):
    """
    The base application exception. All of the exceptions raisen by this 
    application should be inherited from this exception.
    """

    def __init__(self, title: str, details: dict) -> None:
        """
        Initialize the exception.

        Args:
            title (str): A string that represents the title of an exception.
            details (dict): A dictionary that contains the explicit information about the exception details.
        """
        self.title = title
        self.details = details
