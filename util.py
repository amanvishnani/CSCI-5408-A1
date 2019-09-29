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
        <{}> 
        <name>{}</name>
        <id>{}</id>
        <{}/>
        """.format(table_name, key, obj[key], table_name)

    return """<?xml version="1.0"?>
    <list> {} </list>
    """.format(xml)


def save_to_file(text: str, file_name: str):
    try:
        f = open("out/" + file_name, "w+", encoding="utf-8")
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


def get_building_id(address: str, input_file="./out/building.xml"):
    try:
        file = open(input_file, 'r', encoding="utf-8")
        string = file.read()
        soup = BeautifulSoup(string, features="html.parser")
        b_list = soup.find_all("building")
        for b in b_list:
            b_addr = b.find_next("address").get_text()
            if b_addr in address:
                return b.find_next("id").get_text()
    except Exception as e:
        print(e)
        return None


def get_department_id(name_of_dept):
    return generic_search(name_of_dept, "department", "name", "./out/department.xml", "id")


def get_faculty_id(name_of_faculty):
    return generic_search(name_of_faculty, "faculty", "name", "./out/faculty.xml", "id")


def get_campus_id(name_of_faculty):
    return generic_search(name_of_faculty, "campus", "name", "./out/campus.xml", "id")


def generic_search(text: str, row_tag, lookup_by_tag, input_file, return_tag):
    try:
        file = open(input_file, 'r', encoding="utf-8")
        string = file.read()
        soup = BeautifulSoup(string, features="html.parser")
        my_list = soup.find_all(row_tag)
        for b in my_list:
            search_string = b.find_next(lookup_by_tag).get_text()
            if text in search_string:
                return b.find_next(return_tag).get_text().strip()
    except Exception as e:
        print(e)
        return ""


def dal_prefix(url: str):
    if not url.startswith("http"):
        return "https://dal.ca" + url
    else:
        return url
