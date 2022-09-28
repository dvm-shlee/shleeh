#!/usr/scripts/env python
"""
Helper for python module develop for dvm-shlee
"""
from distutils.core import setup
from setuptools import find_packages
import re, io

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    io.open('shleeh/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

__author__ = 'SungHo Lee'
__email__ = 'shlee@unc.edu'
__url__ = 'https://github.com/dvm-shlee/shleeh'

setup(name='shleeh',
      version=__version__,
      description='Helper for python module develop for dvm-shlee',
      python_requires='>3.5',
      author=__author__,
      author_email=__email__,
      url=__url__,
      license='GNLv3',
      packages=find_packages(),
      install_requires=[],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows :: Windows 10',
          'Programming Language :: Python :: >3.5',
          'Topic :: Software Development',
      ],
      keywords='personal helper'
     )
