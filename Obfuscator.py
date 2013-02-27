from EdiDocument import EdiDocument


class Obfuscator:
    def obfuscate(self, ediDocument=EdiDocument()):
        self.ediDocument = ediDocument
        self.__obfuscate_sender_ids()
        self.__obfuscate_receiver_ids()
        self.__obfuscate_control_ids()

        return self.ediDocument


    def __obfuscate_sender_ids(self):
        id_value = "OBFUSCATE34AA  "
        self.ediDocument.interchange.header.isa06.content = id_value
        self.ediDocument.interchange.groups[0].header.gs02.content = id_value


    def __obfuscate_receiver_ids(self):
        id_value = "OBFUSCATE78BB  "
        self.ediDocument.interchange.header.isa08.content = id_value
        self.ediDocument.interchange.groups[0].header.gs03.content = id_value

    def __obfuscate_control_ids(self):
        control_id = "OBF456789"
        self.ediDocument.interchange.header.isa13.content = control_id
        self.ediDocument.interchange.trailer.iea02.content = control_id
        self.ediDocument.interchange.groups[0].header.gs06.content = control_id
        self.ediDocument.interchange.groups[0].trailer.ge02.content = control_id