from EdiValidationErrors import Error

class Report():
    """A Base report class"""
    pass


class ValidationReport(Report):

    def __init__(self):
        self.error_list=[]

    def add_error(self, error=Error()):
        self.error_list.append(error)