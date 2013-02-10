import unittest
from Fixtures import FixtureReader, FixtureFiles
from EdiValidator import Validator

class TestSimple810DocumentInterchange(unittest.TestCase):

    def setUp(self):
        self.document = FixtureReader().read_edi_file(FixtureFiles.simple_810_file)

    def test_810_interchange_header_isa01(self):
        """Ensure the isa01 field is read correctly"""
        self.assertEqual("00", self.document.interchange.header.isa01.content)

    def test_810_interchange_header_isa02(self):
        """Ensure the isa02 field is read correctly"""
        self.assertEqual("          ", self.document.interchange.header.isa02.content)

    def test_810_interchange_header_isa03(self):
        """Ensure the isa03 field is read correctly"""
        self.assertEqual("00", self.document.interchange.header.isa03.content)

    def test_810_interchange_header_isa04(self):
        """Ensure the isa04 field is read correctly"""
        self.assertEqual("          ", self.document.interchange.header.isa04.content)

    def test_810_interchange_header_isa05(self):
        """Ensure the isa05 field is read correctly"""
        self.assertEqual("12", self.document.interchange.header.isa05.content)

    def test_810_interchange_header_isa06(self):
        """Ensure the isa06 field is read correctly"""
        self.assertEqual("8005551234AA   ", self.document.interchange.header.isa06.content)

    def test_810_interchange_header_isa07(self):
        """Ensure the isa07 field is read correctly"""
        self.assertEqual("12", self.document.interchange.header.isa07.content)

    def test_810_interchange_header_isa08(self):
        """Ensure the isa08 field is read correctly"""
        self.assertEqual("8005556789BB   ", self.document.interchange.header.isa08.content)

    def test_810_interchange_header_isa09(self):
        """Ensure the isa09 field is read correctly"""
        self.assertEqual("131031", self.document.interchange.header.isa09.content)

    def test_810_interchange_header_isa10(self):
        """Ensure the isa10 field is read correctly"""
        self.assertEqual("1518", self.document.interchange.header.isa10.content)

    def test_810_interchange_header_isa11(self):
        """Ensure the isa11 field is read correctly"""
        self.assertEqual("U", self.document.interchange.header.isa11.content)

    def test_810_interchange_header_isa12(self):
        """Ensure the isa12 field is read correctly"""
        self.assertEqual("00401", self.document.interchange.header.isa12.content)

    def test_810_interchange_header_isa13(self):
        """Ensure the isa13 field is read correctly"""
        self.assertEqual("000007777", self.document.interchange.header.isa13.content)

    def test_810_interchange_header_isa14(self):
        """Ensure the isa14 field is read correctly"""
        self.assertEqual("0", self.document.interchange.header.isa14.content)

    def test_810_interchange_header_isa15(self):
        """Ensure the isa15 field is read correctly"""
        self.assertEqual("P", self.document.interchange.header.isa15.content)

    def test_810_interchange_header_isa16(self):
        """Ensure the isa14 field is read correctly"""
        self.assertEqual(">", self.document.interchange.header.isa16.content)

    def test_810_interchange_trailer_iea01(self):
        """Ensure the iea01 field is read correctly"""
        self.assertEqual("1", self.document.interchange.trailer.iea01.content)

    def test_810_interchange_trailer_iea02(self):
        """Ensure the iea02 field is read correctly"""
        self.assertEqual("000007777", self.document.interchange.trailer.iea02.content)


class TestSimple810DocumentGroup(unittest.TestCase):

    def setUp(self):
        self.document = FixtureReader().read_edi_file(FixtureFiles.simple_810_file)

    def test_810_group_header_gs01(self):
        """Ensure the gs01 field is read correctly"""
        self.assertEqual("IN", self.document.interchange.groups[0].header.gs01.content)

    def test_810_group_header_gs02(self):
        """Ensure the gs02 field is read correctly"""
        self.assertEqual("8005551234A", self.document.interchange.groups[0].header.gs02.content)

    def test_810_group_header_gs03(self):
        """Ensure the gs03 field is read correctly"""
        self.assertEqual("8005556789B", self.document.interchange.groups[0].header.gs03.content)

    def test_810_group_header_gs04(self):
        """Ensure the gs04 field is read correctly"""
        self.assertEqual("20121126", self.document.interchange.groups[0].header.gs04.content)

    def test_810_group_header_gs05(self):
        """Ensure the gs05 field is read correctly"""
        self.assertEqual("1610", self.document.interchange.groups[0].header.gs05.content)

    def test_810_group_header_gs06(self):
        """Ensure the gs06 field is read correctly"""
        self.assertEqual("8234", self.document.interchange.groups[0].header.gs06.content)

    def test_810_group_header_gs07(self):
        """Ensure the gs07 field is read correctly"""
        self.assertEqual("X", self.document.interchange.groups[0].header.gs07.content)

    def test_810_group_header_gs07(self):
        """Ensure the gs08 field is read correctly"""
        self.assertEqual("004010", self.document.interchange.groups[0].header.gs08.content)

    def test_810_group_trailer_ge01(self):
        """Ensure the ge01 field is read correctly"""
        self.assertEqual("1", self.document.interchange.groups[0].trailer.ge01.content)

    def test_810_group_trailer_ge02(self):
        """Ensure the ge02 field is read correctly"""
        self.assertEqual("8234", self.document.interchange.groups[0].trailer.ge02.content)

class TestSimple810DocumentTransactionSet(unittest.TestCase):

    def setUp(self):
        self.document = FixtureReader().read_edi_file(FixtureFiles.simple_810_file)

    def test_810_group_header_st01(self):
        """Ensure the st01 field is read correctly"""
        self.assertEqual("810", self.document.interchange.groups[0].transaction_sets[0].header.st01.content)

    def test_810_group_header_st02(self):
        """Ensure the st02 field is read correctly"""
        self.assertEqual("000000001", self.document.interchange.groups[0].transaction_sets[0].header.st02.content)

    def test_810_group_header_st03(self):
        """Ensure the st03 field is read correctly"""
        self.assertEqual("", self.document.interchange.groups[0].transaction_sets[0].header.st03.content)

    def test_810_group_trailer_se01(self):
        """Ensure the se01 field is read correctly"""
        self.assertEqual("12", self.document.interchange.groups[0].transaction_sets[0].trailer.se01.content)

    def test_810_group_trailer_se02(self):
        """Ensure the se02 field is read correctly"""
        self.assertEqual("000000001", self.document.interchange.groups[0].transaction_sets[0].trailer.se02.content)

class TestSimple810Validation(unittest.TestCase):
    def setUp(self):
        self.document = FixtureReader().read_edi_file(FixtureFiles.simple_810_file)

    def test_simple_810_validation(self):
        out = Validator().is_valid_document(self.document)
        self.assertTrue(out)

if __name__ == '__main__':
    unittest.main()
