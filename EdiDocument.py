from Interchange import Interchange

class EdiDocument():
    """An EDI X12 document"""
    def __init__(self):
        self.document_text = ""
        self.element_separator="*"
        self.segment_terminator="~"
        self.sub_element_separator=">"
        self.version="00401"
        self.interchange = Interchange()



