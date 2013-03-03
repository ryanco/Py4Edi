
class Configuration(object):
    pass


class EdiDocumentConfiguration(Configuration):

    def __init__(self, version, element_separator, segment_terminator, sub_element_separator):
        """Creates a new Edi Document Configuration"""
        Configuration.__init__(self)
        self.version = version
        self.element_separator = element_separator
        self.segment_terminator = segment_terminator
        self.sub_element_separator = sub_element_separator