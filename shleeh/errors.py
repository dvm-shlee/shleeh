import os


class Error(Exception):
    """ Base class for other custom exceptions """
    message = None


class FileNotValidError(Error):
    """ Raised when the file is not valid format """
    def __init__(self, file_name=None, data_type=None):
        self.file_name = None
        self.data_type = None

        if file_name is not None:
            self.file_name = os.path.basename(file_name)
            if os.path.isdir(file_name):
                object_type = 'directory'
            else:
                object_type = 'file'
            if data_type is not None:
                self.data_type = data_type
                self.message = "The {} '{}' is not valid {}".format(object_type,
                                                                    self.file_name,
                                                                    self.data_type)
            else:
                self.message = "The {} '{}' is not valid".format(object_type,
                                                                 self.file_name)
        else:
            self.message = "The file is not valid"


class ArchiveFailedError(Error):
    """ Raised when the archive process is failed [designed for brkraw module] """
    file_name = None

    def __init__(self, file_name=None):
        if file_name is not None:
            self.file_name = os.path.basename(file_name)
            self.message = "The data '{}' is not archived".format(self.file_name)
        else:
            self.message = "Archive failed to execute"


class RemoveFailedError(Error):
    """ Raise when the os.remove process is failed """
    file_name = None

    def __init__(self, file_name=None):
        if file_name is not None:
            self.file_name = os.path.basename(file_name)
            self.message = "The file '{}' is not removed".format(self.file_name)
        else:
            self.message = "Remove failed to execute"


class RenameFailedError(Error):
    """ Raised when the os.rename process is failed (OSError)"""
    file1_name = None
    file2_name = None

    def __init__(self, file1_name=None, file2_name=None):
        if file1_name is not None:
            self.file1_name = os.path.basename(file1_name)
        if file2_name is not None:
            self.file2_name = os.path.basename(file2_name)
        if (self.file1_name is not None) and (self.file2_name is not None):
            self.message = "Rename failed to execute from:'{}' to:'{}'".format(self.file1_name,
                                                                               self.file2_name)
        else:
            self.message = "Rename failed to execute"


class UnexpectedError(Error):
    """ Raised when unexpected error occurred """
    def __init__(self, message=None):
        if message is None:
            self.message = "Unexpected error"
        else:
            self.message = message
