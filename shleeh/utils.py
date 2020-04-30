import re
import pip
import time
import warnings
import pkg_resources


class TimeCounter:
    _start = None

    def __init__(self):
        self.reset()

    def reset(self):
        self._start = time.time()

    def time(self):
        return time.time() - self._start


def upgrade(*modules: list):
    pip.main(['install', '--upgrade'] + modules)


def install(*args):
    pip.main(['install'] + args)


def get_installed_pkg(regex=None):
    if regex is None:
        return [p for p in pkg_resources.working_set]
    else:
        pattern = re.compile(regex)
        return [p for p in pkg_resources.working_set if pattern.search(p.project_name) is not None]


def deprecated_warning(dep_func, alt_func, future=False):
    # def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    #     return '%s: %s\n' % (category.__name__, message)
    if future:
        category = PendingDeprecationWarning
        tense = 'will be'
    else:
        category = DeprecationWarning
        tense = 'is'

    # warnings.formatwarning = warning_on_one_line
    warnings.simplefilter("default")
    warnings.warn(f"{dep_func} {tense} deprecated. Please use {alt_func} instead.", category,
                  stacklevel=2)
    warnings.simplefilter("ignore")

