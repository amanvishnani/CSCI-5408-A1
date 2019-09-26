class BaseEntity:
    def __init__(self, id=None):
        self.id: int = id;

    def to_xml_obj(self):
        raise Exception("Method not implemented")
