from buildingScraping import scrape_buildings
from campusservicesScraping import scrapeCampusServices
from libraryScraping import scrape_libraries_services
from eventScraping import scrapeGlobalEvents
from facultyAndDeptScraping import scrape_faculty, scrapeDepartment
from scrape_staff import scrape_staff_main
from scrapePrograms import scrapeUndergraduatePrograms


scrape_buildings()
scrapeCampusServices()
scrape_libraries_services()
scrapeGlobalEvents()
scrape_faculty()
scrapeDepartment()
scrape_staff_main()
scrapeUndergraduatePrograms()