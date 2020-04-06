class Error(Exception):
    """ Base class for other custom exceptions """
    pass


class FileNotValidError(Error):
    """ Raised when the file is not valid format """
    def __init__(self, file_name, data_type):
        self.file_name = file_name
        self.data_type = data_type


