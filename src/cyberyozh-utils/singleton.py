# -*- coding: utf-8 -*-


class Singleton(type):

    """
    A metaclass that creates a Singleton base class when called.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Wraps constructor and calls it only for the first time
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
