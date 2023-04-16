import pkg_resources
import re


def get_installed_pkg(regex=None):
    if regex is None:
        return [p for p in pkg_resources.working_set]
    else:
        pattern = re.compile(regex)
        return [p for p in pkg_resources.working_set if pattern.search(p.project_name) is not None]
