# -*- coding: utf-8 -*-
import time

from datetime import datetime


def get_current_time():
    """
    :return: current Unix time plus duration
    """
    return int(time.mktime(datetime.now().timetuple()))


def add_time_delta(duration):
    """
    :return: moment in future; current Unix time plus duration delta
    """
    return get_current_time() + int(duration)


def subtract_time_delta(duration):
    """
    :return: moment in past; current Unix time minus duration delta
    """
    return get_current_time() - int(duration)
