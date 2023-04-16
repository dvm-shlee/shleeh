import warnings


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
