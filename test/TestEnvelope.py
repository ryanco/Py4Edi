import unittest
from Envelope import Envelope
from Segment import Segment
from Element import Element
from Configuration import EdiDocumentConfiguration

class TestEnvelope(unittest.TestCase):

    def test_envelope_format_as_edi_no_body(self):
        envelope=MockEnvelope()
        cfg = EdiDocumentConfiguration("00401", "|", "\n", ">")
        edi_string = "HDR|12|123456\nTLR|1|123456\n"
        self.assertEqual(edi_string, envelope.format_as_edi(cfg))

    def test_envelope_format_as_edi_with_bod(self):
        envelope = MockEnvelopeWithBody()
        cfg = EdiDocumentConfiguration("00401", "|", "\n", ">")
        edi_string = "HDR|12|123456\nBDY|14|123\nBDZ|1|123\nTLR|1|123456\n"
        self.assertEqual(edi_string, envelope.format_as_edi(cfg))

class MockEnvelope(Envelope):

    def __init__(self):
        Envelope.__init__(self)
        self.header=MockHeaderSegment()
        self.trailer=MockTrailerSegment()

class MockEnvelopeWithBody(Envelope):

    def __init__(self):
        Envelope.__init__(self)
        self.header=MockHeaderSegment()
        self.trailer=MockTrailerSegment()
        self.items=self.body
        self.items.append(MockBDYHeaderSegment())
        self.items.append(MockBDZTrailerSegment())


class MockHeaderSegment(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCKHDR",
            description="Mock Header",
            required=True, minLength=2, maxLength=3, content="HDR")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="12")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="123456")
        self.fields.append(self.test02)


class MockTrailerSegment(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCKTRL",
            description="Mock Trailer",
            required=True, minLength=2, maxLength=3, content="TLR")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="1")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="123456")
        self.fields.append(self.test02)

class MockBDYHeaderSegment(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCKBDY",
            description="Mock Body Header",
            required=True, minLength=2, maxLength=3, content="BDY")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="14")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="123")
        self.fields.append(self.test02)


class MockBDZTrailerSegment(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCKTRL",
            description="Mock Body Trailer",
            required=True, minLength=2, maxLength=3, content="BDZ")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="1")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="123")
        self.fields.append(self.test02)

if __name__ == '__main__':# pragma: no cover
    unittest.main()