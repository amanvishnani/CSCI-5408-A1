from util import *
from models.CampusService import CampusService
from models.WebLinks import WebLinks
from models.XmlList import XmlList

soup = get_soup('https://www.dal.ca/faculty_staff.html')
service_nodes = soup.find_all("h4", class_="c-title")
ServiceList: List[CampusService] = list()
WebLinkList: List[WebLinks] = list()

for node in service_nodes:
    link_nodes = node.find_next("ul").find_all("li");
    service = node.find_next("h4").find_next("a")
    service_url = service.get("href")
    service_name = service.get_text()
    campusService = CampusService(service_name, service_url)
    ServiceList.append(campusService)
    for link_node in link_nodes:
        link = link_node.find_next("a")
        url = link.get('href')
        text = link.get_text()
        webLink = WebLinks(text, url, service_name)
        WebLinkList.append(webLink)


xmlCampService = XmlList()
xmlCampService.from_list(ServiceList)
xmlCampService.save("campus_service.xml")


xmlWebLinks = XmlList()
xmlWebLinks.from_list(WebLinkList)
xmlWebLinks.save("web_links.xml")