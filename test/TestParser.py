import unittest
from EdiDocument import EdiDocument
from EdiParser import Parser
from ParserErrors import InvalidFileTypeError, SegmentTerminatorNotFoundError

class TestParser(unittest.TestCase):

    def setUp(self):

        self.goodISAWithAsterisk ="ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~"
        self.goodISAWithPipe ="ISA|00|          |00|          |12|8005551234AA   |12|8005556789BB   |110408|1221|U|00401|000006617|0|P|>~"
        self.badISA="PSA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~"
        self.goodISAWithLeadingSpaces="       ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~"
        self.twoSegments="ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~IEA*0*000006617~"
        self.newLineTerminator="ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>\nIEA*0*000006617\n"
        self.extraTerminator="ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~\nIEA*0*000006617~\n"
        self.nonEDIFile="<xml><test></test></xml>"
        self.emptySegmentsWithNoTerminator="ISA****************"
        self.emptySegmentsWithTerminator="ISA****************>~"
        self.edi_with_ISA_GS_GE_IEA="ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~GS*IN*8005551234A*8005556789B*20110408*1221*6617*X*004010~GE*6*6617~IEA*1*000006617"
        self.parser = Parser()

    def test_good_isa_segment_asterisk_separator(self):
        """Test a valid ISA segment"""
        document = self.parser.parse_document(document_text=self.goodISAWithAsterisk)
        self.assertEqual(document.interchange.header.id.name, EdiDocument().interchange.header.id.name)

    def test_good_isa_segment_pipe_separator(self):
        """Test a valid ISA segment"""
        document = self.parser.parse_document(document_text=self.goodISAWithPipe)
        self.assertEqual(document.interchange.header.id.name, EdiDocument().interchange.header.id.name)

    def test_good_isa_segment_version(self):
        """Test a valid ISA segment"""
        document = self.parser.parse_document(document_text=self.goodISAWithAsterisk)
        self.assertEqual(document.version, "00401")

    def test_good_isa_segment_with_leading_spaces(self):
        """Test a valid ISA segment with leading spaces"""
        document = self.parser.parse_document(document_text=self.goodISAWithLeadingSpaces)
        self.assertEqual(document.interchange.header.id.name, EdiDocument().interchange.header.id.name)

    def test_bad_isa_segment(self):
        """Test an invalid ISA segment"""
        self.assertRaises(InvalidFileTypeError, self.parser.parse_document, self.badISA)

    def test_two_segments(self):
        """Test to ensure the parser can find the segment terminator"""
        document = self.parser.parse_document(document_text=self.twoSegments)
        self.assertEqual("00", document.interchange.header.isa01.content)
        self.assertEqual("0", document.interchange.trailer.iea01.content)

    def test_new_line_segment_terminator(self):
        """Test to ensure the parser can find the segment terminator"""
        document = self.parser.parse_document(document_text=self.newLineTerminator)
        self.assertEqual("00", document.interchange.header.isa01.content)
        self.assertEqual("0", document.interchange.trailer.iea01.content)

    def test_extra_line_segment_terminator(self):
        """Test to ensure the parser can find the segment terminator"""
        document = self.parser.parse_document(document_text=self.newLineTerminator)
        self.assertEqual("00", document.interchange.header.isa01.content)
        self.assertEqual("0", document.interchange.trailer.iea01.content)
        self.assertEqual(document.interchange.trailer.id.name, EdiDocument().interchange.trailer.id.name)

    def test_non_edi_document(self):
        """Test an invalid EDI document"""
        self.assertRaises(InvalidFileTypeError, self.parser.parse_document, self.nonEDIFile)

    def test_empty_segments_no_terminator(self):
        """Test a document with all empty ISA segments and no segment terminator"""
        self.assertRaises(SegmentTerminatorNotFoundError, self.parser.parse_document, self.emptySegmentsWithNoTerminator)

    def test_empty_segments_with_terminator(self):
        """Test to ensure the parser can find the segment terminator"""
        document = self.parser.parse_document(document_text=self.emptySegmentsWithTerminator)
        self.assertEqual("", document.interchange.header.isa01.content)

    def test_isa_gs_ge_iea(self):
        """Test a document with an ISA, GS, GE, and IEA segment"""
        document = self.parser.parse_document(document_text=self.edi_with_ISA_GS_GE_IEA)
        self.assertEqual("00", document.interchange.header.isa01.content)
        self.assertEqual("1", document.interchange.trailer.iea01.content)

