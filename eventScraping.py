import urllib3
from models.Event import *
from bs4 import BeautifulSoup

http = urllib3.PoolManager()


def getGlobalEvents():
    finalList = list();

    for i in range(1, 12):
        try:
            url = 'https://www.dal.ca/news/events/_jcr_content/contentPar/eventslisting.month.html/2019-{}-01.html'.format(i);
            r = http.request('GET',
                             url)
            soup = BeautifulSoup(r.data, features="html.parser")
            events = soup.findAll("div", class_="h4-placeholder")
            for event in events:
                date = event.h4.get_text().strip();
                link = event.find("a").get("href").strip();
                time = event.find("dd").get_text().strip();
                name = event.find("a").get_text().strip();
                eventObj = Event(name, date,time, link)
                eventObj = getEventDetails(eventObj);
                finalList.append();
        except Exception as e: print(e)
    return finalList;

def getEventDetails(event):
    r = http.request('GET', event.link)
    soup = BeautifulSoup(r.data, features="html.parser");

    description = soup.find("h1").find_next("p");
    event.description = description.get_text().strip();

    category = description.find_next("h4").find_next("p");
    event.category = category.get_text().strip();

    time = category.find_next("h4").find_next("p");
    endIdx = time.get_text().index("Ends:")
    event.startTime = time.get_text()[:endIdx].strip()[8:]
    event.endTime = time.get_text()[endIdx:].strip()[6:]

    location = time.find_next('h4').find_next('p');
    event.location = location.get_text().strip();

    cost = location.find_next("h4").find_next("p");
    event.cost = cost.get_text().strip();
    return event;

testEvent = Event(None, None, None, "https://www.dal.ca/news/events/2019/10/31/the_cuban_revolution_at_60___international_conference.html");
getEventDetails(testEvent)

# events = getGlobalEvents();
# print(len(events));