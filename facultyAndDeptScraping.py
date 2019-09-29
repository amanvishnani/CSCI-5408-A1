from models.XmlList import XmlList
from util import *
from models.Faculty import Faculty
from models.Department import Department


def scrape_faculty():
    print("*************** Scraping Faculty *********************")
    url = 'https://www.dal.ca/academics/faculties.html';
    soup = get_soup(url)
    main_div = soup.find_all("div", class_="text parbase section")
    f_list = list()

    for child in main_div:
        if is_faculty(child):
            name = child.find_next("h2").get_text().strip()
            href = child.find_next("h2").find_next('a').get("href").strip()
            if not href.startswith("http"):
                href = "https://dal.ca" + href
            faculty = Faculty(name, href)
            f_list.append(faculty)
    generate_id(f_list)
    XmlList().from_list(f_list).save("faculty.xml")


def is_faculty(node):
    if node.find_next("h2").get_text().strip() == "Choose from 13 diverse Faculties":
        return False

    if "parbase" in node.get("class"):
        return True
    pass


def scrapeDepartment():
    print("*************** Scraping Departments *********************")
    url = 'https://www.dal.ca/academics/faculties.html'
    soup = get_soup(url)
    main_div = soup.find_all("div", class_="expandingSubsection section")
    d_list = list()

    for child in main_div:
        a_tags = child.find_all("a")
        for a_tag in a_tags:
            txt = a_tag.get_text().strip()
            link = a_tag.get('href')
            d_list.append(Department(txt, link))
        pass
    generate_id(d_list)
    XmlList().from_list(d_list).save("departments.xml")
