from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class CampusService(BaseIdentityEntity):
    name = ""
    web_page_url = ""

    def __init__(self, name, web_page_url):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.web_page_url = web_page_url

    def to_xml_obj(self):
        xml_obj = XmlObject("campus_service")
        xml_obj.add("name", self.name)
        xml_obj.add("web_page_url", self.web_page_url)
        return xml_obj
