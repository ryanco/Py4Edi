from Envelope import GroupEnvelope
from Element import Element
from Segment import Segment

class Group(GroupEnvelope):
    """An EDI X12 groups"""
    def __init__(self):
        GroupEnvelope.__init__(self)
        self.header= GroupHeader()
        self.trailer=GroupTrailer()

class GroupHeader(Segment):
    """An EDI X12 groups header"""
    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=8

        self.id=Element(name="GS",
            description="Functional Group Header Code",
            required=True, minLength=2, maxLength=2, content="GS")
        self.fields.append(self.id)

        self.gs01=Element(name="GS01",
            description="Functional Identifier Code",
            required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.gs01)

        self.gs02=Element(name="GS02",
            description="Application Senders Code",
            required=True, minLength=2, maxLength=15, content="")
        self.fields.append(self.gs02)

        self.gs03=Element(name="GS03",
            description="Application Receiver Code",
            required=True, minLength=2, maxLength=15, content="")
        self.fields.append(self.gs03)

        self.gs04=Element(name="GS04",
            description="Group Date",
            required=True, minLength=8, maxLength=8, content="")
        self.fields.append(self.gs04)

        self.gs05=Element(name="GS05",
            description="Group Time",
            required=True, minLength=4, maxLength=4, content="")
        self.fields.append(self.gs05)

        self.gs06=Element(name="GS06",
            description="Group Control Number",
            required=True, minLength=1, maxLength=9, content="")
        self.fields.append(self.gs06)

        self.gs07=Element(name="GS07",
            description="Responsible Agency Code",
            required=True, minLength=1, maxLength=2, content="")
        self.fields.append(self.gs07)

        self.gs08=Element(name="GS08",
            description="Version Indicator ID Code",
            required=True, minLength=1, maxLength=12, content="")
        self.fields.append(self.gs08)



class GroupTrailer(Segment):
    """An EDI X12 groups trailer"""
    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2

        self.id=Element(name="GE",
            description="Functional Group Trailer Identifier",
            required=True, minLength=2, maxLength=2, content="")
        self.fields.append(self.id)

        self.ge01=Element(name="GE01",
            description="Number of Transaction Sets",
            required=True, minLength=1, maxLength=6, content="")
        self.fields.append(self.ge01)

        self.ge02=Element(name="GE02",
            description="Group Control Number",
            required=True, minLength=1, maxLength=9, content="")
        self.fields.append(self.ge02)
