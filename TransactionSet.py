from Envelope import TransactionSetEnvelope
from Element import Element
from Segment import Segment

class TransactionSet(TransactionSetEnvelope):
    """An EDI X12 transaction set"""
    def __init__(self):
        TransactionSetEnvelope.__init__(self)
        self.header= TransactionSetHeader()
        self.trailer=TransactionSetTrailer()


class TransactionSetHeader(Segment):
    """The transaction set header"""
    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=3

        self.id=Element(name="ST",
                description="Transaction Set Header",
                required=True, minLength=2, maxLength=2, content="ST")
        self.fields.append(self.id)
    
        self.st01=Element(name="ST01",
            description="Transaction Set ID Code",
            required=True, minLength=3, maxLength=3, content="")
        self.fields.append(self.st01)

        self.st02=Element(name="ST02",
            description="Transaction Set Control Number",
            required=True, minLength=4, maxLength=9, content="")
        self.fields.append(self.st02)
    
        self.st03=Element(name="ST03",
            description="Implementation Convention Reference",
            required=False, minLength=1, maxLength=35, content="")
        self.fields.append(self.st03)


class TransactionSetTrailer(Segment):
    """The transaction set header"""
    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2

        self.id=Element(name="SE",
            description="Transaction Set Trailer",
            required=True, minLength=2, maxLength=2, content="SE")
        self.fields.append(self.id)

        self.se01=Element(name="SE01",
            description="Number of Included Segments",
            required=True, minLength=1, maxLength=6, content="")
        self.fields.append(self.se01)

        self.se02=Element(name="SE02",
            description="Transaction Set Control Number",
            required=True, minLength=4, maxLength=9, content="")
        self.fields.append(self.se02)