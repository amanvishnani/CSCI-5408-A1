from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject


class Program(BaseIdentityEntity):
    def __init__(self, name, level, web_page):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.level = level
        self.web_page = web_page
        self.faculty_id = ""
        self.department_id = ""
        self.campus_id = ""
        self.program_length = ""
        self.program_start = ""

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("program")
        xml_obj.add('name', self.name)
        xml_obj.add('level', self.level)
        xml_obj.add("web_page", self.web_page)
        xml_obj.add("faculty_id", self.faculty_id)
        xml_obj.add("department_id", self.department_id)
        xml_obj.add('campus_id', self.department_id)
        xml_obj.add('id', self.id)
        return xml_obj
