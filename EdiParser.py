from EdiDocument import EdiDocument
from Group import Group, GroupHeader, GroupTrailer
from TransactionSet import TransactionSet, TransactionSetHeader, TransactionSetTrailer
from ParserErrors import InvalidFileTypeError, SegmentTerminatorNotFoundError


class Parser:
    def __init__(self):
        """Create a new Parser"""
        self.ediDocument = EdiDocument()


    def parse_document(self, document_text=""):
        """Parse the text document into an object
        :param document_text:  the text to parse into an EDI document.
        """
        self.documentText = document_text.lstrip()
        #attach the original document text to the document.
        self.ediDocument.document_text = self.documentText

        if self.documentText.startswith(EdiDocument().interchange.header.id.name):
            self.__parse_interchange_header()
            self.__separate_and_route_segments()

        else:
            foundSegment = self.documentText[:3]
            raise InvalidFileTypeError(segment=foundSegment,
                                       msg="Expected Element Envelope: " + EdiDocument().interchange.header.id.name +
                                           " but found Element Envelope: " + foundSegment +
                                           ".\n The length of the expected segment is: " + str(
                                           len(EdiDocument().interchange.header.id.name)) +
                                           " the length of the segment found was: " + str(len(foundSegment)))

        return self.ediDocument

    def __parse_interchange_header(self):
        """Parse the interchange header segment"""
        header = self.ediDocument.interchange.header
        #The edi separator is always at position 4
        self.ediDocument.document_configuration.element_separator = self.documentText[3:4]
        headerFieldList = self.documentText.split(self.ediDocument.document_configuration.element_separator)
        for index, isa in enumerate(headerFieldList):
            if index == 12:
                self.ediDocument.version = isa
            if index <= 15:
                header.fields[index].content = isa
            if index == 16:
                lastHeaderField = headerFieldList[16]
                #the sub-element separator is always the first character in this element.
                header.isa16.content = lastHeaderField[0:1]
                if lastHeaderField[1:2]:
                    self.ediDocument.document_configuration.segment_terminator = lastHeaderField[1:2]
                else:
                    raise SegmentTerminatorNotFoundError(
                        msg="The segment terminator is not present in the Interchange Header, can't parse file.")


    def __separate_and_route_segments(self):
        """Handles separating all the segments"""
        self.segment_list = self.documentText.split(self.ediDocument.document_configuration.segment_terminator)
        for segment in self.segment_list:
            self.__route_segment_to_parser(segment)

    def __route_segment_to_parser(self, segment):
        """Take a generic segment and determine what segment to parse it as
        :param segment:
        """
        if segment.startswith(GroupHeader().id.name):
            self.__parse_group_header(segment)
        elif segment.startswith(GroupTrailer().id.name):
            self.__parse_group_trailer(segment)
        elif segment.startswith(EdiDocument().interchange.trailer.id.name):
            self.__parse_interchange_trailer(segment)
        elif segment.startswith(TransactionSetHeader().id.name):
            self.__parse_transaction_set_header(segment)
        elif segment.startswith(TransactionSetTrailer().id.name):
            self.__parse_transaction_set_trailer(segment)
        else:
            pass

    def __parse_segment(self, segment, segmentFieldList):
        """Generically parse segments
        :param segment:
        :param segmentFieldList:
        """
        for index, gs in enumerate(segmentFieldList):
            segment.fields[index].content = gs

    def __parse_group_header(self, segment):
        """Parse the group header"""
        self.current_group = Group()
        header = GroupHeader()
        headerFieldList = segment.split(self.ediDocument.document_configuration.element_separator)
        self.__parse_segment(header, headerFieldList)
        self.current_group.header = header

    def __parse_group_trailer(self, segment):
        """Parse the group trailer"""
        trailer = GroupTrailer()
        trailerFieldList = segment.split(self.ediDocument.document_configuration.element_separator)
        self.__parse_segment(trailer, trailerFieldList)
        self.current_group.trailer = trailer
        self.ediDocument.interchange.groups.append(self.current_group)

    def __parse_interchange_trailer(self, segment):
        """Parse the interchange trailer segment"""
        trailer = self.ediDocument.interchange.trailer
        trailerFieldList = segment.split(self.ediDocument.document_configuration.element_separator)
        self.__parse_segment(trailer, trailerFieldList)

    def __parse_transaction_set_header(self, segment):
        """Parse transaction set header
        Creates a new transaction set and set it as the current transaction set.
        """
        self.current_transaction = TransactionSet()
        transactionHeader = TransactionSetHeader()
        headerFieldList = segment.split(self.ediDocument.document_configuration.element_separator)
        self.__parse_segment(transactionHeader, headerFieldList)
        self.current_transaction.header = transactionHeader

    def __parse_transaction_set_trailer(self, segment):
        """Parse the transaction set trailer.
        Adds the completed transaction to a edi document.
        """
        transactionTrailer = TransactionSetTrailer()
        trailerFieldList = segment.split(self.ediDocument.document_configuration.element_separator)
        self.__parse_segment(transactionTrailer, trailerFieldList)
        self.current_transaction.trailer = transactionTrailer
        self.current_group.transaction_sets.append(self.current_transaction)
