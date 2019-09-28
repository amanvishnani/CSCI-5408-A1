from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class Library(BaseIdentityEntity):
    def __init__(self, name="", link="", note="", address=""):
        BaseIdentityEntity.__init__(self)
        self.name: str = name
        self.website: str = link
        self.note: str = note
        self.address: str = address
        self.building_id = None

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("library")
        xml_obj.add("name", self.name)
        xml_obj.add("website", self.website)
        xml_obj.add("note", self.note)
        xml_obj.add("address", self.address)
        xml_obj.add("id", self.id)
        xml_obj.add("building_id", self.building_id)
        return xml_obj

