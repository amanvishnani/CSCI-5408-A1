from models.Event import *
from models.XmlList import XmlList
from util import *

http = urllib3.PoolManager()


def get_global_events():
    xml_list = XmlList()
    final_list: List[Event] = list()
    base_url = 'https://www.dal.ca/news/events/_jcr_content/contentPar/eventslisting.month.html/2019-{}-01.html'
    for i in range(1, 12):
        try:
            url = base_url.format(i)
            r = http.request('GET', url)
            soup = BeautifulSoup(r.data, features="html.parser")
            dal_event_nodes = soup.findAll("div", class_="h4-placeholder")
            for event_node in dal_event_nodes:
                link = event_node.find("a").get("href").strip()
                name = event_node.find("a").get_text().strip()
                event_obj = Event(name, link)
                print("GET - {}".format(event_obj.name))
                event_obj = get_event_details(event_obj)
                final_list.append(event_obj)
        except Exception as e:
            print(e)
    generate_id(final_list)
    xml_list.from_list(final_list)
    return xml_list


def clean_location(location: str):
    location = location.replace("Ave,", "Avenue,")
    return location


def get_event_details(event):
    try:
        soup = get_soup(event.link)

        if soup is None:
            return

        description = soup.find("h1").find_next("p")
        if description is not None:
            event.description = description.get_text().strip()

        category = soup.find("h4", string="Category")
        if category is not None:
            category = category.find_next("p")
            event.category = category.get_text().strip()
        else:
            event.category = ""

        time = soup.find("h4", string="Time").find_next("p")
        if time is not None:
            txt = time.get_text().strip()
            if txt.startswith("Start"):
                end_idx = txt.index("Ends:")
                event.start_date_time = txt[:end_idx].strip()[8:]
                event.end_date_time = txt[end_idx:].strip()[6:]
            else:
                event.start_date_time = time.get_text().strip()
                event.end_date_time = time.get_text().strip()

        location = soup.find('h4', string="Location")
        if location is not None:
            location = location.find_next('p')
            event.location = location.get_text().strip()
            event.location = clean_location(event.location)
            b_id = get_building_id(location)
            if b_id is not None:
                event.building_id = b_id

        cost = soup.find("h4", string="Cost")
        if cost is not None:
            cost = cost.find_next("p")
            event.cost = cost.get_text().strip()
    except Exception as e:
        print(e)
    return event


def scrapeGlobalEvents():
    print("*************** Scraping Global Events *********************")
    dal_events = get_global_events()
    dal_events.save("event.xml")
