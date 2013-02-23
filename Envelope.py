from Segment import Segment
from Reports import ValidationReport

class Envelope(object):

    def __init__(self):
        self.header=Segment()
        self.trailer=Segment()
        self.body=[]

    def format_as_edi(self, document_configuration):
        document=self.header.format_as_edi(document_configuration)
        document+=self.__format_body_as_edi(document_configuration)
        document+=self.trailer.format_as_edi(document_configuration)
        return document

    def __format_body_as_edi(self, document_configuration):
        document=""
        for item in self.body:
            document+=item.format_as_edi(document_configuration)
        return document

    def validate(self):
        report = ValidationReport()
        self.header.validate()
        self.__validate_body()
        self.trailer.validate()
        return report

    def __validate_body(self):
        for item in self.body:
            item.validate()

class InterchangeEnvelope(Envelope):

    def __init__(self):
        Envelope.__init__(self)
        self.groups=self.body


class GroupEnvelope(Envelope):

    def __init__(self):
        Envelope.__init__(self)
        self.transaction_sets=self.body


class TransactionSetEnvelope(Envelope):

    def __init__(self):
        Envelope.__init__(self)
        self.transaction_body=self.body