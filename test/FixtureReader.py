from EdiParser import Parser

class FixtureReader():

    def read_edi_document(self, file_path):
        handle = open(file_path, 'r')
        try:
            edi_text = handle.read()
            edi_document = Parser().parse_document(document_text=edi_text)
        finally:
            handle.close()

        return edi_document
