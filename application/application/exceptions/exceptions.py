from domain.exceptions import BaseException


class ApplicationException(BaseException):
    """
    The base application layer exception. All of the exceptions risen
    due to errors occured while business logic execution should be inherited
    from this exception.
    """


class MemoryIsFullException(ApplicationException):
    """
    This exception should be raisen if the in-memory storage limit is exceeded.
    """


class LinkNotFoundException(ApplicationException):
    """
    This exception should be raisen if a full link was not found.
    """
