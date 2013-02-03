
class Element(object):
    """A generic segment"""
    def __init__(self, name="", description="", required="", minLength="", maxLength="", content=""):
        self.name = name
        self.description = description
        self.required = required
        self.minLength = minLength
        self.maxLength = maxLength
        self.content = content

    def is_valid(self):
        """Validate the segment"""

        content_length = len(self.content)
        if content_length < self.minLength:
            return False, "Field "+self.name+" is too short. Found "+str(content_length)\
                          +" characters, expected "+str(self.minLength)+" characters."
        if content_length > self.maxLength:
            return False, "Field "+self.name+" is too long. Found "+str(content_length)\
                          +" characters, expected "+str(self.maxLength)+" characters."

        return True, ""

    def __str__(self):
        return str(self.content)