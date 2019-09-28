from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class Department(BaseIdentityEntity):
    def __init__(self, name, website):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.website = website
        self.course_prefix = ""
        self.faculty_id = ""

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("department")
        xml_obj.add("name", self.name)
        xml_obj.add("website", self.website)
        xml_obj.add("course_prefix", self.course_prefix)
        xml_obj.add("faculty_id", self.faculty_id)
        xml_obj.add("id", self.id)
        return xml_obj