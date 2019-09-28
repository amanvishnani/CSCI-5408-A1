from models.XmlObject import XmlObject
from models.Library import Library
from models.BaseIdentityEntity import BaseIdentityEntity


class LibraryService(BaseIdentityEntity):
    def __init__(self, name="", website="", image_url="", address="", building_id=0, library=None):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.website = website
        self.image_url = image_url
        self.address = address
        self.building_id: int = building_id
        self.library: Library = library

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("library_service")
        xml_obj.add("name", self.name)
        xml_obj.add("website", self.website)
        xml_obj.add("image_url", self.image_url)
        xml_obj.add("address", self.address)
        xml_obj.add("building_id", self.building_id)
        xml_obj.add("id", self.id)
        if self.library is not None:
            xml_obj.add("library_id", self.library.id)
        return xml_obj

