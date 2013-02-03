from Interchange import Interchange

class EdiDocument():
    """An EDI X12 document"""
    element_separator="*"
    segment_terminator="~"
    sub_element_separator=">"

    def __init__(self):
        self.document_text = ""
        self.element_separator=EdiDocument.element_separator
        self.segment_terminator=EdiDocument.segment_terminator
        self.sub_element_separator=EdiDocument.sub_element_separator
        self.version="00401"
        self.interchange = Interchange()

    def format_as_edi(self):
        return self.interchange.format_as_edi(self.element_separator,
            self.segment_terminator, self.sub_element_separator)




