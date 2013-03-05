from EdiValidationErrors import FieldValidationError

class Element(object):
    """A generic segment"""

    def __init__(self, name="", description="", required="", minLength="", maxLength="", content=""):
        self.name = name
        self.description = description
        self.required = required
        self.minLength = minLength
        self.maxLength = maxLength
        self.content = content

    def validate(self, report):
        """Validate the element"""
        if self.required or self.content!="":
            content_length = len(self.content)
            self.__is_field_too_short(content_length, report)
            self.__is_field_too_long(content_length, report)

    def __str__(self):
        if self.required:
            return str(self.content)

        if self.content != "":
            return str(self.content)

        return ""

    def __is_field_too_short(self, content_length, report):
        """
        Determine if the field content is too short.
        :param content_length: current content length.
        :param report: the validation report to append errors.
        """
        if content_length < self.minLength:
            report.add_error(
                FieldValidationError(msg="Field " + self.name + " is too short. Found " + str(content_length) \
                                         + " characters, expected " + str(self.minLength) + " characters.",
                                     segment=self))

    def __is_field_too_long(self, content_length, report):
        """
        Determine if the field content is too long.
        :param content_length: current content length.
        :param report: the validation report to append errors.
        """
        if content_length > self.maxLength:
            report.add_error(FieldValidationError(msg="Field " + self.name + " is too long. Found " + str(content_length) \
                                                  + " characters, expected " + str(self.maxLength) + " characters.",
                                                  segment=self))
