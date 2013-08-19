import proc
from setuptools import setup, find_packages
import os

DIRNAME = os.path.dirname(os.path.abspath(__file__))

setup(
    name = 'proc',
    version = '0.1',
    packages = find_packages(),
    install_requires = [],
    entry_points = {},
    author = 'Denis "thuck" Doria',
    author_email = 'denisdoria@gmail.com',
    description = '',
    license = 'GPLv3',
    keywords = 'proc',
    url = 'https://github.com/thuck/proc',
)
