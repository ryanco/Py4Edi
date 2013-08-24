import abc
from Document import Document


class Parser(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def parse_text(self, text_to_parse):
        return Document()


class DocumentParser(Parser):

    def parse_text(self, text_to_parse):
        return Document()


class EdiDocumentParser(DocumentParser):

    def parse_text(self, text_to_parse):
        return Document()


class InterchangeParser(Parser):

    def parse_text(self, text_to_parse):
        return Document()


