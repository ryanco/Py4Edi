from EdiParser import Parser

class Fixtures():
    pass

class FixtureFiles():
    simple_edi_file="fixtures/General/Simple.edi"
    interchange_control_id_mismatch_error_document='fixtures/validation_errors/InterchangeControlIDMismatch.edi'
    multiple_groups_file='fixtures/General/MultipleGroups.edi'
    single_group_multiple_transactions_file='fixtures/General/MultipleTransactions.edi'


class FixtureReader():

    def read_edi_file(self, file_path):
        """Read in a file and parse it to an EDI document

        Attributes:
            file_path -- path to the file to read.
        """
        handle = open(file_path, 'r')

        try:
            edi_text = handle.read()
            edi_document = Parser().parse_document(document_text=edi_text)
        finally:
            handle.close()

        return edi_document
