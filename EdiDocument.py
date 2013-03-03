from Interchange import Interchange
from Configuration import EdiDocumentConfiguration
from Settings import CurrentSettings
from Reports import ValidationReport


class EdiDocument():
    """An EDI X12 document"""

    def __init__(self):
        self.document_text = ""
        self.document_configuration = EdiDocumentConfiguration(CurrentSettings.version,
                                                               CurrentSettings.element_separator,
                                                               CurrentSettings.segment_terminator,
                                                               CurrentSettings.sub_element_separator)
        self.interchange = Interchange()

    def format_as_edi(self):
        """Format this document as EDI and return it as a string"""
        return self.interchange.format_as_edi(self.document_configuration)

    def validate(self):
        """Validate this document and return a validation report"""
        report = ValidationReport()
        self.interchange.validate(report)
        return report




