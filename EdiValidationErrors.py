class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class FieldValidationError(Error):
    """Exception raised for errors in the input.

    Attributes:
        segment -- segment in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, segment, msg):
        self.segment = segment
        self.msg = msg


class IDMismatchError(Error):
    """Exception raised for errors in the input.

        Attributes:
            segment -- segment in which the error occurred
            msg  -- explanation of the error
        """

    def __init__(self, segment, msg):
        self.segment = segment
        self.msg = msg
