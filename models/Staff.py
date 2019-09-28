from models.People import People
from models.XmlObject import XmlObject



class Staff(People):
    def __init__(self, first_name, last_name, salutation, position):
        People.__init__(self, first_name, last_name, salutation)
        self.position = position
        self.department_id = ""

    def to_xml_obj(self) -> XmlObject:
        xml_obj = XmlObject("teaching_staff")
        xml_obj.add('position', self.position)
        xml_obj.add('department_id', self.department_id)
        xml_obj.add('id', self.id)
        return xml_obj

