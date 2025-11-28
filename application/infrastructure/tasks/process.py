from threading import get_native_id
from urllib.parse import urlparse

from infrastructure.enums import Procedure
from infrastructure.flags import storing_allowed
from infrastructure.logging import base_logger
from infrastructure.repository import in_memory_repository
from infrastructure.shortener import Shortener
from interface_adapters.controllers import RetriveUrlController, ShortenUrlController


def process(user_input: str) -> str:
    """
    This task is the thin transportation layer which responsibilities
    are very similar to the responsibilities of an endpoint in a web server.

    It's main task is processing the user input and transmission of the data
    to the inner layers of the application.

    It also validates the input.
    """
    os_thread_id = get_native_id()

    base_logger.info(f'Your task will be processed in the thread with ID {os_thread_id}')
    base_logger.info(f'Your input was {user_input}')

    if storing_allowed.is_set():

        splitted_input = user_input.split(',')

        if len(splitted_input) != 2:
            base_logger.info('Input is invalid. It should only contain a single coma.')
        else:
            procedure, link = [item.strip() for item in splitted_input]

            parsed_link = urlparse(url=link)

            try:
                _, _, _ = parsed_link[:3]
            except IndexError:
                base_logger.info('The provided link is invalid.')
            else:
                if procedure == Procedure.SHORTEN:
                    controller = ShortenUrlController(link=link, repo=in_memory_repository, shortener=Shortener())
                    return controller.shorten()
                elif procedure == Procedure.RETRIEVE:
                    controller = RetriveUrlController(link=link, repo=in_memory_repository)
                    return controller.retrieve_link()

    else:
        base_logger.info(f'Storage capacity is exceeded. The operation can not be executed at this time.')
