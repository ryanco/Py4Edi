class Settings(object):
    pass


class DefaultSettings(Settings):
    """Default settings defined"""
    element_separator = "*"
    segment_terminator = "~"
    sub_element_separator = ">"
    version = "00401"


class CurrentSettings(Settings):
    """Current Settings"""
    element_separator = DefaultSettings.element_separator
    segment_terminator = DefaultSettings.segment_terminator
    sub_element_separator = DefaultSettings.sub_element_separator
    version = DefaultSettings.version





