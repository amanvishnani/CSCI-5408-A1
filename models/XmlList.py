from typing import List
from models.XmlObject import XmlObject
from models.BaseEntity import BaseEntity


class XmlList:
    data: List[XmlObject] = list()
    tag_name: str = "list"

    def __int__(self, tag_name: str = "list"):
        self.tag_name = tag_name
        self.data = []

    def add(self, value: XmlObject):
        self.data.append(value)

    def __str__(self, xml_meta=True):
        xml = '<?xml version="1.0"?>\n'
        elements = ''
        for obj in self.data:
            elements = elements + "{}\n".format(obj.__str__())
        return "{}<{}> {} </{}>".format(xml, self.tag_name, elements, self.tag_name);

    def from_list(self, obj_list: List[BaseEntity]):
        for obj in obj_list:
            self.add(obj.to_xml_obj())

    def save(self, file_name: str):
        try:
            f = open(file_name, "w+")
            f.write(self.__str__())
            f.close()
        except Exception as e:
            print(e)