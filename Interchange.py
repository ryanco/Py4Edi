from Envelope import InterchangeEnvelope
from Segment import Segment
from Element import Element
from EdiValidationErrors import IDMismatchError


class Interchange(InterchangeEnvelope):
    """An EDI X12 interchange"""

    def __init__(self):
        InterchangeEnvelope.__init__(self)
        self.header = InterchangeHeader()
        self.trailer = InterchangeTrailer()

    def validate(self, report):
        if self.header.isa13.content != self.trailer.iea02.content:
            isa13_desc = self.header.isa13.description
            isa13_name = self.header.isa13.name
            iea02_desc = self.trailer.iea02.description
            iea02_name = self.trailer.iea02.name
            report.add_error(IDMismatchError(
                msg="The " + isa13_desc + " in " + isa13_name + " does not match " + iea02_desc + " in " + iea02_name,
                segment=self.header.id))


class InterchangeHeader(Segment):
    """An EDI X12 interchange header"""

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount = 16

        self.id = Element(name="ISA",
                          description="Interchange Control Header Code",
                          required=True, minLength=3, maxLength=3, content="ISA")
        self.fields.append(self.id)

        self.isa01 = Element(name="ISA01",
                             description="Authorization Information Qualifier",
                             required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.isa01)

        self.isa02 = Element(name="ISA02",
                             description="Authorization Information",
                             required=True, minLength=10, maxLength=10, content="")
        self.fields.append(self.isa02)

        self.isa03 = Element(name="ISA03",
                             description="Security Information Qualifier",
                             required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.isa03)

        self.isa04 = Element(name="ISA04",
                             description="Security Information",
                             required=True, minLength=10, maxLength=10, content="")
        self.fields.append(self.isa04)

        self.isa05 = Element(name="ISA05",
                             description="Interchange ID Qualifier",
                             required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.isa05)

        self.isa06 = Element(name="ISA06",
                             description="Interchange Sender ID",
                             required=True, minLength=15, maxLength=15, content="")
        self.fields.append(self.isa06)

        self.isa07 = Element(name="ISA07",
                             description="Interchange ID Qualifier",
                             required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.isa07)

        self.isa08 = Element(name="ISA08",
                             description="Interchange Receiver ID",
                             required=True, minLength=15, maxLength=15, content="")
        self.fields.append(self.isa08)

        self.isa09 = Element(name="ISA09",
                             description="Interchange Date",
                             required=True, minLength=6, maxLength=6, content="")
        self.fields.append(self.isa09)

        self.isa10 = Element(name="ISA10",
                             description="Interchange Time",
                             required=True, minLength=4, maxLength=4, content="")
        self.fields.append(self.isa10)

        self.isa11 = Element(name="ISA11",
                             description="Interchange Control Standard ID",
                             required=True, minLength=1, maxLength=1, content="")
        self.fields.append(self.isa11)

        self.isa12 = Element(name="ISA12",
                             description="Interchange Control Version Number",
                             required=True, minLength=5, maxLength=5, content="")
        self.fields.append(self.isa12)

        self.isa13 = Element(name="ISA13",
                             description="Interchange Control Number",
                             required=True, minLength=9, maxLength=9, content="")
        self.fields.append(self.isa13)

        self.isa14 = Element(name="ISA14",
                             description="Acknowledgement Requested Flag",
                             required=True, minLength=1, maxLength=1, content="")
        self.fields.append(self.isa14)

        self.isa15 = Element(name="ISA15",
                             description="Test Indicator",
                             required=True, minLength=1, maxLength=1, content="")
        self.fields.append(self.isa15)

        self.isa16 = Element(name="ISA16",
                             description="Sub-element Separator",
                             required=True, minLength=1, maxLength=1, content="")
        self.fields.append(self.isa16)


class InterchangeTrailer(Segment):
    """An EDI X12 interchange Trailer"""

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount = 2

        self.id = Element(name="IEA",
                          description="Interchange Control Trailer Code",
                          required=True, minLength=3, maxLength=3, content="")
        self.fields.append(self.id)

        self.iea01 = Element(name="IEA01",
                             description="Number of Included Groups",
                             required=True, minLength=1, maxLength=5, content="")
        self.fields.append(self.iea01)

        self.iea02 = Element(name="IEA02",
                             description="Interchange Control Number",
                             required=True, minLength=1, maxLength=9, content="")
        self.fields.append(self.iea02)


