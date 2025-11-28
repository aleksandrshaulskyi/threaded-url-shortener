from enum import Enum


class Procedure(str, Enum):
    """
    This dataclass is used to manage the procedure parameter from the user input.
    """
    SHORTEN = 's'
    RETRIEVE = 'r'
