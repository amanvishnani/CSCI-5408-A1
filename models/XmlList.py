from typing import List
from models.XmlObject import XmlObject
from models.BaseIdentityEntity import BaseIdentityEntity
from bs4 import  BeautifulSoup


class XmlList:
    xml_list = list()
    tag_name = "list"

    def __int__(self, tag_name: str = "list"):
        self.tag_name = tag_name
        self.xml_list = list()

    def add(self, value: XmlObject):
        self.xml_list.append(value)

    def __str__(self, xml_meta=True):
        xml = '<?xml version="1.0"?>\n'
        elements = ''
        for obj in self.xml_list:
            elements = elements + "{}\n".format(obj.__str__())
        return "{}<{}> {} </{}>".format(xml, self.tag_name, elements, self.tag_name);

    def from_list(self, obj_list: List[BaseIdentityEntity]):
        for obj in obj_list:
            self.add(obj.to_xml_obj())
        return self;

    def save(self, file_name: str):
        try:
            f = open("out/"+file_name, "w+", encoding="utf-8")
            xml = self.__str__()
            soup = BeautifulSoup(xml, features="html.parser")
            f.write(soup.prettify())
            f.close()
        except Exception as e:
            print(e)