# -*- coding: utf-8 -*-

import os
import pathlib
from distutils.dir_util import copy_tree

from .log_helper import logger

PROJECT_DIR = os.path.join(os.path.realpath(__file__), "..")
HOME_DIR = os.path.join(pathlib.Path.home())


def home_dir():
    """
    :return: Current user home dir
    """
    return HOME_DIR


def load_config_path(self, config_dir, config_filename):
    """
    :return : absolute file path in HOME config directory
    """
    config_path = os.path.join(home_dir(), config_dir, config_filename)
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"File {config_filename} is not found in {self.home_dir}")
    return config_path


class ConfigLoader:

    """
    '.auditor_srv' is config dir for IP Auditor server library
    '.auditor_client' is config dir for check_ip.py utility
    '.auditor_mock' is config for Auditor mock server
    """

    def __init__(self):
        """
        Path to HOME config dir and where config files should come from
        """
        self.home_dir = os.path.join(pathlib.Path.home())
        logger.info(f"Config home dir: {self.home_dir}")

    def install_default_config(self, config_dir, source_dir):
        """
        If config_dir does not exist, create it and copy source_dir content there
        :param config_dir:
        :param source_dir:
        """
        home_config_path = os.path.join(self.home_dir, config_dir)
        source_path = os.path.abspath(source_dir)
        if not os.path.isdir(home_config_path):
            os.mkdir(home_config_path)
            copy_tree(source_path, home_config_path)

