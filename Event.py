

class Event:
    name = None
    date = None
    startTime = None
    endTime = None
    link = None
    location = None
    cost = None
    category = None
    additionalInformation = None
    description = None
    def __init__(self, name, date, time, link):
        self.name = name;
        self.date = date;
        self.startTime = time
        self.link = link
        pass
