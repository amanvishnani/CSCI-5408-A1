from models.Person import Person
from models.XmlObject import XmlObject


class Staff(Person):
    def __init__(self, first_name, last_name, salutation, position):
        Person.__init__(self, first_name, last_name, salutation)
        self.position = position
        self.department_id = ""

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("teaching_staff")
        xml_obj.add('position', self.position)
        xml_obj.add('department_id', self.department_id)
        xml_obj.add('net_id', self.id)
        xml_obj.add('is_ta', "0")
        return xml_obj
