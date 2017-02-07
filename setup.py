import sys
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

import univider

PACKAGE = "univider"
NAME = "univider"
DESCRIPTION = "yet another web spider interface"
AUTHOR = "taoyang"
AUTHOR_EMAIL = "ty@puton.info"
URL = "http://puton.info"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    packages=find_packages(),
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'univider=univider.handler:main'
        ]
    },

)