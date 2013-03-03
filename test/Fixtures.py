from EdiParser import Parser


class Fixtures(object):
    pass


class FixtureReader(Fixtures):
    def read_edi_file(self, file_path):
        """Read in a file and parse it to an EDI document

        Attributes:
            file_path -- path to the file to read.
        """
        handle = open(file_path, 'r')

        try:
            edi_text = handle.read()
            edi_document = Parser().parse_document(document_text=edi_text)
            FixtureFiles.documents[file_path] = edi_document
        finally:
            handle.close()

        return edi_document


class FixtureFiles(Fixtures):
    documents = {}
    simple_edi_file = "fixtures/General/Simple.edi"
    interchange_control_id_mismatch_error_file = 'fixtures/validation_errors/InterchangeControlIDMismatch.edi'
    interchange_included_group_count_error_file = 'fixtures/validation_errors/InterchangeIncludedGroupsCountError.edi'
    groups_included_transaction_count_error_file = 'fixtures/validation_errors/GroupIncludedTransactionCountError.edi'
    multiple_groups_file = 'fixtures/General/MultipleGroups.edi'
    single_group_multiple_transactions_file = 'fixtures/General/MultipleTransactions.edi'
    simple_810_file = 'fixtures/810/Simple810.edi'

    def load_documents(self):
        FixtureReader().read_edi_file(FixtureFiles.simple_edi_file)
        FixtureReader().read_edi_file(FixtureFiles.interchange_control_id_mismatch_error_file)
        FixtureReader().read_edi_file(FixtureFiles.interchange_included_group_count_error_file)
        FixtureReader().read_edi_file(FixtureFiles.groups_included_transaction_count_error_file)
        FixtureReader().read_edi_file(FixtureFiles.multiple_groups_file)
        FixtureReader().read_edi_file(FixtureFiles.single_group_multiple_transactions_file)
        FixtureReader().read_edi_file(FixtureFiles.simple_810_file)

