from util import *
from models.Building import Building
from typing import List

campus_ids = dict()

def scrapeBuildings():
    pass

def getBuildings(campus_ids) -> List[Building]:
    if campus_ids is None:
        campus_ids = dict()
    url = "https://www.dal.ca/content/dalhousie/en/home/campus-maps/building-directory/_jcr_content/contentPar/autosearcher.filterResults.ajax";
    building_list: List[Building] = list();
    building_soup = getSoup(url);
    buildings = building_soup.find_all("dt");
    for buildingDt in buildings:
        building_url = buildingDt.find("a").get("href").strip();
        building_detail = getBuildingDetail(building_url, campus_ids)
        building_list.append(building_detail);

    return building_list;


def add_campus(campus_ids, campus):
    if(not campus_ids):
        campus_ids[campus] = 1
        return
    maxVal = max(campus_ids.values())
    campus_ids[campus] = maxVal+1;


def getBuildingDetail(url, campus_ids) -> Building:
    if campus_ids is None:
        campus_ids = dict()
    url = "https://dal.ca"+url
    amenities = dict();

    building_detail_soup = getSoup(url)
    campus = building_detail_soup.find("li", class_="open").find("a").get_text();
    campus_id = campus_ids.get(campus);
    if campus_id is None:
        add_campus(campus_ids, campus);
        campus_id = campus_ids.get(campus);
    sub_content = building_detail_soup.find("div", class_="subsite-content");
    name_h1 = building_detail_soup.find("h1");
    name = name_h1.get_text();
    address_p = name_h1.find_next("p");
    address = address_p.get_text();
    pointer = address_p.find_next("p")
    img = pointer.find_next("img");
    img_url = img.get("src");
    description_p = pointer.find_next("p");
    description = description_p.get_text()
    amenities_table = sub_content.find_next("table");
    trs = amenities_table.find_all("tr");
    for tr in trs:
        amenities[tr.find("th").get_text()] = tr.find("td").get_text();

    return Building(name, address, description, img_url, amenities);

getBuildingDetail("/campus-maps/building-directory/agricultural-campus/beef-barn.html", campus_ids)
getBuildingDetail("/campus-maps/building-directory/studley-campus/1312-robie.html", campus_ids)
# getBuildings()