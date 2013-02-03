from Segment import Segment

class Envelope(object):

    def __init__(self):
        self.header=Segment()
        self.trailer=Segment()

    def format_as_edi(self, element_separator, segment_terminator, sub_element_separator):
        document=self.header.format_as_edi(element_separator, segment_terminator, sub_element_separator)
        document+=self.trailer.format_as_edi(element_separator, segment_terminator, sub_element_separator)
        return document

    def format_as_edi(self, element_separator, segment_terminator, sub_element_separator, children):
        document=self.header.format_as_edi(element_separator, segment_terminator, sub_element_separator)
        document+=self.format_children_as_edi(element_separator, segment_terminator, sub_element_separator, children)
        document+=self.trailer.format_as_edi(element_separator, segment_terminator, sub_element_separator)
        return document

    def format_children_as_edi(self, element_separator, segment_terminator, sub_element_separator, children):
            document=""
            for child in children:
                document+=child.format_as_edi(element_separator, segment_terminator, sub_element_separator)
            return document

class InterchangeEnvelope(Envelope):

    def __init__(self):
        self.groups=[]
        Envelope.__init__(self)

    def format_as_edi(self, element_separator, segment_terminator, sub_element_separator):
        return super(InterchangeEnvelope, self).format_as_edi(element_separator,
            segment_terminator, sub_element_separator, self.groups)


class GroupEnvelope(Envelope):

    def __init__(self):
        self.transaction_sets=[]
        Envelope.__init__(self)

    def format_as_edi(self, element_separator, segment_terminator, sub_element_separator):
        return super(GroupEnvelope, self).format_as_edi(element_separator,
            segment_terminator, sub_element_separator, self.transaction_sets)
