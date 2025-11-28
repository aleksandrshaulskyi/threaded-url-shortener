# No GIL (free threaded) url shortener service.

A simple url-shortener service written in clean architecture using free-threaded python (3.14t).

## Brief.

With 3.14 Python released in october 2025, it was interesting for me to get my hands on the new version.

I do understand that such task does not require any significant computational resources at all and it would be hard
to notice the difference, but still, it was a fun and in fact quite educational process that helped me
to find out few new details about threading and it's implementation in Python.

## Features.

A simple service that uses the command line as the interface. Hints are provided at the most vital steps.

Basically supports 2 features.

- Shortening urls.
- Retrieving the full versions of such urls by their shortened counterparts.

The capacity of the storage is artificially limited in order to test and demonstrate
the importance of lock mechanisms in the free threaded applications.

## Test it yourself.

- Fork the repo.
- Execute main.py.
