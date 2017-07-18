# -*- coding: utf-8 -*-
"""
setup.py file for Redacted.
"""
### #------------------------------------------------------------------------
### Imports
### #------------------------------------------------------------------------
# Standard Library
from setuptools import setup, find_packages
import logging

# Third Party

# Package / Application
from package import (
    __version__,
    __project_url__,
    __package_name__,
    __description__,
    __long_descr__,
)

# turn off logging if we're going to build a distribution
logging.disable(logging.CRITICAL)

setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=__long_descr__,
    packages=find_packages(),
    author="Douglas Thor",
    url=__project_url__,
    classifiers=[
        "Development Status :: 1 - Planning",
        ],
    requires=[
    ],
)
