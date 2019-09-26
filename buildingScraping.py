from util import *
from models.Building import Building
from typing import List, Dict

campus_ids = dict()


def build_ids(obj: Dict[str, int]):
    i = 1
    for key in obj.keys():
        obj[key] = i
        i = i + 1
    pass


def dict_to_xml_rows(obj: Dict[str, int], table_name: str):
    xml = ""
    for key in obj.keys():
        xml = xml + """
        <{} name="{}" id="{}"/>
        """.format(table_name, key, obj[key])

    return "<list> {} </list>".format(xml)


def scrape_buildings(campus_ids):
    buildings = get_buildings(campus_ids)
    i = 1
    amenities: Dict[str, int] = dict()
    for b in buildings:
        for key in b.amenities.keys():
            amenities[key] = 1
        b.id = i
        i = i + 1
        amenities.pop("Accessibilty")  # clean data
    build_ids(amenities)
    save_to_file(dict_to_xml_rows(amenities, "amenity"), "amenity.xml")
    save_to_file(dict_to_xml_rows(campus_ids, "campus"), "campus.xml")


def save_to_file(text: str, file_name: str):
    try:
        f = open(file_name, "w+")
        f.write(text)
        f.close()
    except Exception as e:
        print(e)


def get_buildings(campus_ids) -> List[Building]:
    if campus_ids is None:
        campus_ids = dict()
    url = "https://www.dal.ca/content/dalhousie/en/home/campus-maps/building-directory/_jcr_content/contentPar/autosearcher.filterResults.ajax"
    building_list: List[Building] = list()
    building_soup = getSoup(url)
    buildings = building_soup.find_all("dt")
    i = 0
    for buildingDt in buildings:
        building_url = buildingDt.find("a").get("href").strip()
        building_name = buildingDt.find("a").get_text()
        print("{}. Get Building Detail {}".format(i, building_name))
        building_detail = get_building_detail(building_url, campus_ids)
        building_list.append(building_detail)
        i = i + 1

    return building_list


def add_campus(campus_ids, campus):
    if not campus_ids:
        campus_ids[campus] = 1
        return
    max_val = max(campus_ids.values())
    campus_ids[campus] = max_val + 1


def get_building_detail(url, campus_ids) -> Building:
    if campus_ids is None:
        campus_ids = dict()
    url = "https://dal.ca" + url
    amenities = dict()

    building_detail_soup = getSoup(url)
    campus = building_detail_soup.find("li", class_="open").find("a").get_text()
    campus_id = campus_ids.get(campus)
    if campus_id is None:
        add_campus(campus_ids, campus)
        campus_id = campus_ids.get(campus)
    sub_content = building_detail_soup.find("div", class_="subsite-content")
    name_h1 = building_detail_soup.find("h1")
    name = name_h1.get_text()
    address_p = name_h1.find_next("p")
    address = address_p.get_text()
    pointer = address_p.find_next("p")
    img = pointer.find_next("img")
    img_url = img.get("src")
    description_p = pointer.find_next("p")
    description = description_p.get_text()
    amenities_table = sub_content.find_next("h3").find_next("table")
    trs = amenities_table.find_all("tr")
    for tr in trs:
        amenities[tr.find("th").get_text()] = tr.find("td").get_text()

    return Building(name, address, description, img_url, amenities, campus_id)


# scrape_buildings(campus_ids)

test_dict = {'Studley Campus': 1, 'Sexton Campus': 2, "University of King's College": 3, 'Agricultural Campus': 4,
             'Carleton Campus': 5}
save_to_file(dict_to_xml_rows(test_dict, "campus"), "campus.xml")
