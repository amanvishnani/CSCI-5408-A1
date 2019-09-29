from util import *
from models.Staff import Staff
from models.Staff import Person
from models.XmlList import XmlList


def scrape_medicine_staff():
    soup = get_soup('https://medicine.dal.ca/departments/department-sites/medicine/our-people/faculty.html')
    divs = soup.find_all("div", class_="expandingSubsection section")
    s_list = list()
    dept_id = get_department_id("Department of Medicine")
    for section in divs:
        trs = section.find_all("tr")
        for row in trs:
            name = row.find_next("td").find_next("a").get_text().strip().split(" ")
            position = row.find_next("td").find_next("td").get_text().strip()
            salutation = name.pop(0)
            last_name = name.pop(-1)
            first_name = " ".join(name)
            staff = Staff(first_name, last_name, salutation, position)
            s_list.append(staff)
    return s_list


def scrape_anesthesia_staff():
    soup = get_soup('https://medicine.dal.ca/departments/department-sites/anesthesia/our-people/faculty.html')
    trs = soup.find_all("tr")
    s_list = list()
    dept_id = get_department_id("Department of Anesthesia, Pain Management and Peroperative Medicine")
    for tr in trs:
        name = tr.find_next("td").get_text().strip().split(" ")
        position = tr.find_next("td").find_next("td").get_text().strip()
        staff = Staff(name[0], name[1], "", position)
        staff.department_id = dept_id
        s_list.append(staff)
    generate_id(s_list)
    return s_list


def scrape_staff_main():
    print("*************** Scraping Teaching Staff *********************")
    all_staff = []
    all_people = []
    staff_1 = scrape_anesthesia_staff()
    staff_2 = scrape_medicine_staff()
    all_staff = all_staff + staff_1 + staff_2
    XmlList().from_list(all_staff).save("staff.xml")
    for staff in all_staff:
        p = Person(staff.first_name, staff.last_name, staff.salutation)
        p.id = staff.id
        all_people.append(p)
    XmlList().from_list(all_people).save("person.xml")


# scrape_staff_main()
