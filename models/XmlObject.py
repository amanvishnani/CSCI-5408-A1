from typing import Union


class XmlObject:
    tag_name = "element"

    def __init__(self, tag_name="element"):
        self.tag_name = tag_name
        self.attributes: [str, Union[str, int]] = dict()

    def add(self, key: str, value: Union[str, int]):
        self.attributes[key] = value

    def __str__(self):
        xml = """<{} {} />"""
        attributes = ""
        for key in self.attributes.keys():
            value = self.attributes[key]
            if type(value) is str:
                value = sanitize_xml_data(value)
                attributes = '{} {}="{}"'.format(attributes, key, value)
        return xml.format(self.tag_name, attributes)


def sanitize_xml_data(data: str):
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt")
    data = data.replace(">", "&gt")
    data = data.replace("'", "&apos;")
    data = data.replace('"', "&quot;")
    return data

