class Report():
    """A Base report class"""
    pass


class ValidationReport(Report):

    def __init__(self):
        self.error_list=[]

    def add_error(self, error):
        self.error_list.append(error)

    def is_document_valid(self):
        return len(self.error_list) == 0