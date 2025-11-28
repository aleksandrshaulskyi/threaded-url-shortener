"""
A module that contains a flag that is visible to all threads indicating
that storing link data in the in-memory repository is available.
I.e. storage limit is not exceeded.
"""
from threading import Event


storing_allowed = Event()
storing_allowed.set()
