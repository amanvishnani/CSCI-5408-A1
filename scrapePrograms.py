from util import *
from models.Program import Program
from models.XmlList import XmlList


def scrapeUndergraduatePrograms():
    print("*************** Scraping UG Programs *********************")
    url = "https://www.dal.ca/academics/programs.html"
    soup = get_soup(url)
    programs_tag = soup.find("div", {'id':'node_5c67b3ccd62d40c7884aa43542ff83edcontentPartabcontainerentriestabentry'}).find_all("dt")
    p_list: List[Program] = list()
    for tag in programs_tag:
        name = tag.find("a").get_text()
        web_page = tag.find("a").get('href')
        web_page = dal_prefix(web_page)
        p_soup = get_soup(web_page)
        degree_overview = p_soup.find("h3", string="Degree overview")
        if degree_overview is None:
            continue
        degree_overview = degree_overview.parent.get_text()
        degree_overview = degree_overview.split("\n")
        local_dict = dict()
        for sentence in degree_overview:
            if ("Degree overview" in sentence) or (":" not in sentence):
                continue
            key_val = sentence.split(":")
            local_dict[key_val[0].strip().lower()] = key_val[1].strip()
        p = Program(name, "Undergraduate", web_page)
        faculty = local_dict.get("faculty")
        if faculty.startswith("Faculty of "):
            faculty = faculty.replace("Faculty of ","")
        p.faculty_id = get_faculty_id(faculty)
        p.program_length = local_dict.get("program length")
        p.program_start = local_dict.get("program start")
        if local_dict.get("department") is not None:
            p.department_id = get_department_id(local_dict.get("department"))
        campus = local_dict.get("campus")
        if campus is not None:
            p.campus_id = get_campus_id(campus.strip().split(", ")[0])
        p_list.append(p)
        generate_id(p_list)
    XmlList().from_list(p_list).save("programs.xml")

# scrapeUndergraduatePrograms()