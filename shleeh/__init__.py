"""
version history
 - 0.0.6 : [print_internal_error] method added
"""
from .enums import *
from .utils import *

__all__ = ['__version__',
           'TimeCounter',
           'DataType',
           'get_installed_pkg',
           'deprecated_warning']


__version__ = '0.0.6'
