from EdiDocument import EdiDocument
from EdiValidationErrors import FieldValidationError
from Reports import ValidationReport

class Validator:

    validation_report=ValidationReport()

    def validate_document(self, edi_document):
        self.ediDocument = edi_document
        self.validation_report=self.ediDocument.validate()


        return self.validation_report

    def is_valid_document(self, ediDocument=EdiDocument()):
        """validate the edi document"""
        self.ediDocument = ediDocument
        self.__validate_fields()
        self.__validate_interchange()
        if len(Validator.validation_report.error_list)==0:
            return True
        else:
            return False

    def __validate_fields(self):
        for field in self.ediDocument.interchange.header.fields:
            valid, msg = field.is_valid()
            if not valid:
                raise FieldValidationError(segment=field, msg=msg)
        return True

    def __validate_interchange(self):
        return self.ediDocument.interchange.is_valid()