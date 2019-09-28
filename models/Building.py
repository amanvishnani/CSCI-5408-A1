from models.XmlObject import XmlObject
from models.BaseIdentityEntity import  BaseIdentityEntity
from util import *


class Building(BaseIdentityEntity):

    amenities: Dict[str, str] = dict();

    def __init__(self, name: str, address: str, description: str, image_url: str, amenities: Dict[str, str], campus_id: int):
        BaseIdentityEntity.__init__(self, None)
        self.name = name
        self.address = address
        self.description = description
        if image_url.find("googleads") == -1:
            self.image_url = image_url
        else:
            self.image_url = ""
        self.amenities = amenities
        self.campus_id = campus_id

    def to_xml_obj(self) -> XmlObject:
        obj = XmlObject("building")
        obj.add("name", self.name)
        obj.add("id", self.id)
        obj.add("campus_id", self.campus_id)
        obj.add("address", self.address)
        obj.add("description", self.description)
        obj.add("image_url", self.image_url)
        for key in self.amenities:
            new_key = key.replace(" ","_").lower();
            obj.add(new_key, self.amenities.get(key));

        return obj
