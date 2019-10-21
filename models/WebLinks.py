from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class WebLinks(BaseIdentityEntity):

    def __init__(self, name, link_url, link_name):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.link_url = link_url
        self.link_name = link_name
        self.service_id = ""

    def to_xml_obj(self):
        xml_obj = XmlObject("web_links")
        xml_obj.add("name", self.name)
        xml_obj.add("link_url", self.link_url)
        xml_obj.add("link_name", self.link_name)
        xml_obj.add("service_id", self.service_id)
        return xml_obj

