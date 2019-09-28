from util import *
from models.Staff import Staff
from models.Staff import People
from models.XmlList import XmlList


def scrape_medicine_staff_1():
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
    all_staff = []
    all_people = []
    staff_1 = scrape_medicine_staff_1();
    all_staff = all_staff + staff_1
    XmlList().from_list(all_staff).save("staff.xml")
    for staff in all_staff:
        p = People(staff.first_name, staff.last_name, staff.salutation)
        p.id = staff.id
        all_people.append(p)
    XmlList().from_list(all_people).save("people.xml")


scrape_staff_main()
