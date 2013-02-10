from Interchange import Interchange
from Configuration import EdiDocumentConfiguration

class EdiDocument():
    """An EDI X12 document"""

    def __init__(self):
        self.document_text = ""
        self.document_configuration=EdiDocumentConfiguration(EdiDocumentConfiguration.version,
            EdiDocumentConfiguration.element_separator, EdiDocumentConfiguration.segment_terminator,
            EdiDocumentConfiguration.sub_element_separator)
        self.interchange = Interchange()

    def format_as_edi(self):
        return self.interchange.format_as_edi(self.document_configuration)




