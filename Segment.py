from Element import Element

class Segment(object):
    def __init__(self):
        self.fieldCount = 0
        self.fields = []
        self.id = Element()
        self.element_separator="*"
        self.segment_terminator="~"
        self.sub_element_separator=">"

    def __str__(self):
        out = ""
        if self.__all_fields_empty():
            return out

        for index, field in enumerate(self.fields):
            out += str(field)
            if index<self.fieldCount:
                out+=self.element_separator
            elif index==self.fieldCount:
                out+=self.segment_terminator
        return out

    def format_as_edi(self, element_separator, segment_terminator, sub_element_separator):
        self.element_separator=element_separator
        self.segment_terminator=segment_terminator
        self.sub_element_separator=sub_element_separator
        return str(self)

    def __all_fields_empty(self):
        for field in self.fields:
            if field.content!="":
                return False

        return True