"""
version history
 - 0.0.6 : [print_internal_error] method added
 - 0.0.7 : [add feature] Display directory tree
 - 0.1.0 : [compatibility] remove upper limit restriction of python version
 - 0.1.1 : [compatibility] Added sub-module to __init__.py for easy import
"""
from .enums import *
from .utils import *
from . import errors

__all__ = [
    '__version__',
    'TimeCounter',
    'DataType',
    'get_installed_pkg',
    'deprecated_warning',
    'errors'
    ]


__version__ = '0.1.1'
