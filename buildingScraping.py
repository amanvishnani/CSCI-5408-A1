from util import *
from models.Building import Building
from models.XmlList import XmlList
from typing import List, Dict




def scrape_buildings():
    campus_ids = dict()
    buildings = get_buildings(campus_ids)
    b_list = XmlList()
    amenities: Dict[str, int] = dict()
    generate_id(buildings)
    for b in buildings:
        b_list.add(b.to_xml_obj())
        for key in b.amenities.keys():
            amenities[key] = 1
    build_ids_from_dict(amenities)
    # save_to_file(dict_to_xml_rows(amenities, "amenity"), "amenity.xml")
    save_to_file(dict_to_xml_rows(campus_ids, "campus"), "campus.xml")
    b_list.save("buildings.xml")

def get_buildings(campus_ids) -> List[Building]:
    if campus_ids is None:
        campus_ids = dict()
    url = "https://www.dal.ca/content/dalhousie/en/home/campus-maps/building-directory/_jcr_content/contentPar/autosearcher.filterResults.ajax"
    building_list: List[Building] = list()
    building_soup = get_soup(url)
    buildings = building_soup.find_all("dt")
    i = 0
    for buildingDt in buildings:
        i = i + 1
        building_url = buildingDt.find("a").get("href").strip()
        building_name = buildingDt.find("a").get_text()
        print("{}. Get Building Detail {}".format(i, building_name))
        building_detail = get_building_detail(building_url, campus_ids)
        building_list.append(building_detail)


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

    building_detail_soup = get_soup(url)
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
        key = tr.find("th").get_text().strip()
        value = tr.find("td").get_text().strip()
        if key == "Accessibilty":
            key = "Accessibility";
        amenities[key] = value

    return Building(name, address, description, img_url, amenities, campus_id)


# scrape_buildings()