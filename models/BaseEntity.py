from models.XmlObject import XmlObject


class BaseEntity:
    def __init__(self):
        pass

    def to_xml_obj(self) -> XmlObject:
        raise Exception("Method not implemented")