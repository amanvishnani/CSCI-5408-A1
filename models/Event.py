from models.BaseIdentityEntity import BaseIdentityEntity
from models.XmlObject import XmlObject
from datetime import datetime


class Event(BaseIdentityEntity):
    name = None
    start_date_time = None
    end_date_time = None
    link = None
    location = None
    cost = None
    category = None
    description = None

    def __init__(self, name, link):
        BaseIdentityEntity.__init__(self)
        self.name = name
        self.link = link
        pass

    def to_xml_obj(self):
        xml_obj = XmlObject("event")
        xml_obj.add("id", self.id)
        xml_obj.add("name", self.name)
        start_date_time = ""
        end_date_time = ""
        try:
            dt_obj = datetime.strptime(self.start_date_time, "%A %B %d, %Y - %I:%M %p")
            start_date_time = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        try:
            dt_obj = datetime.strptime(self.end_date_time, "%A %B %d, %Y - %I:%M %p")
            end_date_time = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        xml_obj.add("start_date_time", start_date_time)
        xml_obj.add("end_date_time", end_date_time)
        xml_obj.add("link", self.link)
        xml_obj.add("location", self.location)
        xml_obj.add("category", self.category)
        xml_obj.add("description", self.description)
        xml_obj.add("cost", self.cost)
        return xml_obj

