import re
import time
import warnings
import pkg_resources
from pathlib import Path


class TimeCounter:
    _start = None

    def __init__(self):
        self.reset()

    def reset(self):
        self._start = time.time()

    def time(self):
        return time.time() - self._start


def kill_daemon(daemon_obj):
    if daemon_obj.is_alive():
        if daemon_obj._tstate_lock is not None:
            daemon_obj._tstate_lock.release()
    else:
        pass


def get_installed_pkg(regex=None):
    if regex is None:
        return [p for p in pkg_resources.working_set]
    else:
        pattern = re.compile(regex)
        return [p for p in pkg_resources.working_set if pattern.search(p.project_name) is not None]


def deprecated_warning(dep_func, alt_func, future=False):
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


def user_warning(message):
    warnings.simplefilter("default")
    warnings.warn(message, UserWarning, stacklevel=2)
    warnings.simplefilter("ignore")


def debug_tool(message, fname=None, path=None):
    import os
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%Y%m%d")

    if path is None:
        path = os.path.expanduser('~')
    if fname is None:
        fname = f'debug_{date}'
    with open(os.path.join(path, fname), 'a') as f:
        f.write(message)


def print_internal_error(io_handler=None):
    import traceback, sys
    if io_handler is None:
        io_handler = sys.stderr
    traceback.print_exception(*sys.exc_info(),
                              file=io_handler)


class DirTree(object):
    """
    took from https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
    answered by user: abstrus

    Examples:
        paths = DirTree.make_tree(path)
        for p in paths:
            print(p.displayable())
    """
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if cls._default_criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return isinstance(path, str)

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))