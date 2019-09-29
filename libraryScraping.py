from util import *
from models.Library import Library
from models.LibraryService import LibraryService
from typing import Union
from models.XmlList import XmlList

base_url = 'https://hours.library.dal.ca/'
libraries: List[Library] = list()
services: List[LibraryService] = list()


def populate_details(obj: Union[LibraryService, Library]):
    local_soup = get_soup("{}{}".format(base_url, obj.website))
    div = local_soup.find("div", {'id': obj.website[6:]})
    obj.website = div.find_next("h1").find("a").get('href')
    obj.address = div.find_next("section", class_="contact").find_next("address").find_next("a").get_text()
    obj.building_id = get_building_id(obj.address)
    notes = div.find_next("section", class_="hours").find_next("p", class_='note')
    if notes is not None:
        obj.note = notes.get_text()


def scrape_libraries_services():
    print("*************** Scraping Libraries and Services *********************")
    soup = get_soup(base_url)
    dl = soup.find("dl", {'id': 'locations-table'})
    anchor_nodes = dl.find_all("a")
    last_library = None

    for a_node in anchor_nodes:
        name = a_node.find_next("dt").get_text()
        link = a_node.get('href')
        if name.startswith(' '):
            # is a lib service
            service = LibraryService(name, link)
            service.library = last_library
            populate_details(service)
            services.append(service)
        else:
            # is a lib
            lib = Library(name, link)
            last_library = lib
            populate_details(lib)
            libraries.append(lib)
        generate_id(libraries)
        generate_id(services)
        xml_lib_list = XmlList().from_list(libraries)
        xml_lib_list.save("library.xml")
        xml_services_list = XmlList().from_list(services)
        xml_services_list.save("library_service.xml")


# scrape_libraries_services()
