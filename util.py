import urllib3
from bs4 import BeautifulSoup
from typing import List, Dict

http = urllib3.PoolManager()


def get_soup(url):
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data.decode("utf-8"), features="html.parser")
    return soup;


def get_xml(obj_list: List[object]):
    xml = ''
    for obj in obj_list:
        xml = xml + obj.__str__()
    xml = """<?xml version="1.0"?>
    <list>{}</list>
    """.format(xml)
    return xml;


def build_ids_from_dict(obj: Dict[str, int]):
    i = 1
    for key in obj.keys():
        obj[key] = i
        i = i + 1


def dict_to_xml_rows(obj: Dict[str, int], table_name: str):
    xml = ""
    for key in obj.keys():
        xml = xml + """
        <{} name="{}" id="{}"/>
        """.format(table_name, key, obj[key])

    return """<?xml version="1.0"?>
    <list> {} </list>
    """.format(xml)
