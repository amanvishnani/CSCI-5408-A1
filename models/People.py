from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class People(BaseIdentityEntity):
    def __init__(self, first_name, last_name, salutation):
        BaseIdentityEntity.__init__(self)
        self.first_name = first_name
        self.last_name = last_name
        self.salutation = salutation

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("people")
        xml_obj.add("first_name", self.first_name)
        xml_obj.add("last_name", self.last_name)
        xml_obj.add("id", self.id)
        xml_obj.add("salutation", self.salutation)
        return xml_obj
