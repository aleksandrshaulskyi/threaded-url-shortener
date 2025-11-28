"""
Bunch of simple python loggers that are used to write to stdout.

Yeah. Just because it is more fancy then print.
"""
from logging import getLogger, Formatter, INFO, StreamHandler
from sys import stdout


base_logger = getLogger('application_logger')
base_logger.setLevel(level=INFO)

handler = StreamHandler(stdout)
handler.setFormatter(Formatter('%(asctime)s %(levelname)s %(message)s'))

base_logger.addHandler(handler)
