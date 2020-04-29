import re
import time
import pkg_resources


class TimeCounter():
    _start = None

    def __init__(self):
        self.reset()

    def reset(self):
        self._start = time.time()

    def time(self):
        return time.time() - self._start


def get_installed_pkg(regex=None):
    if regex is None:
        return [p for p in pkg_resources.working_set]
    else:
        pattern = re.compile(regex)
        return [p for p in pkg_resources.working_set if pattern.search(p.project_name) is not None]