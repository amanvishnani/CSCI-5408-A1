import urllib3
from bs4 import BeautifulSoup
from typing import List, Dict
from models.BaseIdentityEntity import BaseIdentityEntity

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

def save_to_file(text: str, file_name: str):
    try:
        f = open("out/"+file_name, "w+", encoding="utf-8")
        soup = BeautifulSoup(text, features="html.parser")
        f.write(soup.prettify())
        f.close()
    except Exception as e:
        print(e)


def generate_id(entities: List[BaseIdentityEntity]):
    i = 1
    for entity in entities:
        entity.id = i
        i += 1


def get_building_id(address: str, input_file="./out/buildings.xml"):
    try:
        file = open(input_file, 'r', encoding="utf-8")
        string = file.read()
        soup = BeautifulSoup(string, features="html.parser")
        b_list = soup.find_all("building")
        for b in b_list:
            b_addr = b.find_next("address").get_text()
            if b_addr in address:
                return int(b.find_next("id").get_text())
    except Exception as e:
        print(e)
        return None

