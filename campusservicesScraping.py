from util import *
from models.CampusService import CampusService
from models.WebLinks import WebLinks
from models.XmlList import XmlList


def scrapeCampusServices():
    print("*************** Scraping Campus Services *********************")
    soup = get_soup('https://www.dal.ca/faculty_staff.html')
    service_nodes = soup.find_all("h4", class_="c-title")
    service_list: List[CampusService] = list()
    web_link_list: List[WebLinks] = list()

    service_id = 0
    for node in service_nodes:
        service_id = service_id + 1
        link_nodes = node.find_next("ul").find_all("li");
        service = node.find_next("h4").find_next("a")
        service_url = service.get("href")
        service_url = dal_prefix(service_url)
        service_name = service.get_text()
        campus_service = CampusService(service_name, service_url)
        campus_service.id = service_id
        service_list.append(campus_service)
        for link_node in link_nodes:
            link = link_node.find_next("a")
            url = link.get('href')
            url = dal_prefix(url)
            text = link.get_text()
            web_link = WebLinks(text, url, service_name)
            web_link.service_id = service_id
            web_link_list.append(web_link)

    xml_camp_service = XmlList()
    xml_camp_service.from_list(service_list)
    xml_camp_service.save("campus_service.xml")

    xml_web_links = XmlList()
    xml_web_links.from_list(web_link_list)
    xml_web_links.save("web_links.xml")
