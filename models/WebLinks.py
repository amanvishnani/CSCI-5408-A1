from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class WebLinks(BaseIdentityEntity):
    link_url = ""
    name = ""
    service_name = ""

    def __init__(self,  name, link_url, service_name):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.link_url = link_url
        self.service_name = service_name

    def to_xml_obj(self):
        xml_obj = XmlObject("web_links")
        xml_obj.add("name", self.name)
        xml_obj.add("link_url", self.link_url)
        xml_obj.add("service_name", self.service_name)
        return xml_obj

