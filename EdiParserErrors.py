class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidFileTypeError(Error):
    """Exception raised for errors in the input.

    Attributes:
        segment -- segment in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, segment, msg):
        self.expr = segment
        self.msg = msg

    def __str__(self):
        return self.msg

class SegmentTerminatorNotFoundError(Error):
    """Exception raised for errors in the Interchange Header.

    Attributes:
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg
