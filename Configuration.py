

class Configuration(object):
    pass

class EdiDocumentConfiguration(Configuration):
    version="00401"
    element_separator="*"
    segment_terminator="~"
    sub_element_separator=">"

    def __init__(self, version, element_separator, segment_terminator, sub_element_separator):
        Configuration.__init__(self)
        self.version=version
        self.element_separator=element_separator
        self.segment_terminator=segment_terminator
        self.sub_element_separator=sub_element_separator