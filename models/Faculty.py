from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class Faculty(BaseIdentityEntity):
    def __init__(self, name, website):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.website = website
        self.dean_id = ""

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("faculty")
        xml_obj.add("name", self.name)
        xml_obj.add("website", self.website)
        xml_obj.add("dean_id", self.dean_id)
        xml_obj.add("id", self.id)
        return xml_obj;