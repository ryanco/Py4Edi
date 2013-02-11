import unittest
from Element import Element
from Segment import Segment

class TestSegment(unittest.TestCase):

    def test_all_required_segment_elements(self):
        segment = MockRequiredSegment()
        self.assertEqual("MCK|TST1|TST2\n", str(segment))

    def test_all_optional_segment_elements_with_some_content_1(self):
        segment = MockOptionalSegment1()
        self.assertEqual("MCK|TST2\n", str(segment))

    def test_all_optional_segment_elements_with_some_content_2(self):
        segment = MockOptionalSegment2()
        self.assertEqual("MCK|TST1\n", str(segment))

    def test_all_optional_segment_elements_with_some_content_3(self):
        segment = MockOptionalSegment3()
        self.assertEqual("TST1\n", str(segment))

    def test_all_optional_segment_elements_with_no_content(self):
        segment = MockOptionalSegment4()
        self.assertEqual("", str(segment))

class MockRequiredSegment(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCK",
            description="Mock Segment ID",
            required=True, minLength=2, maxLength=3, content="MCK")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=True, minLength=1, maxLength=4, content="TST1")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=True, minLength=1, maxLength=4, content="TST2")
        self.fields.append(self.test02)

class MockOptionalSegment1(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCK",
            description="Mock Segment ID",
            required=True, minLength=2, maxLength=3, content="MCK")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="TST2")
        self.fields.append(self.test02)

class MockOptionalSegment2(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCK",
            description="Mock Segment ID",
            required=True, minLength=2, maxLength=3, content="MCK")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="TST1")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="")
        self.fields.append(self.test02)


class MockOptionalSegment3(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCK",
            description="Mock Segment ID",
            required=True, minLength=2, maxLength=3, content="")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="TST1")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="")
        self.fields.append(self.test02)


class MockOptionalSegment4(Segment):

    def __init__(self):
        Segment.__init__(self)
        self.fieldCount=2
        self.element_separator="|"
        self.segment_terminator="\n"

        self.id=Element(name="MOCK",
            description="Mock Segment ID",
            required=True, minLength=2, maxLength=3, content="")
        self.fields.append(self.id)

        self.test01=Element(name="TEST01",
            description="TEST 01 Segment",
            required=False, minLength=1, maxLength=4, content="")
        self.fields.append(self.test01)


        self.test02=Element(name="TEST02",
            description="TEST 02 Segment",
            required=False, minLength=1, maxLength=4, content="")
        self.fields.append(self.test02)

if __name__ == '__main__':# pragma: no cover
    unittest.main()