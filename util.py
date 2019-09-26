import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

def getSoup(url):
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data, features="html.parser")
    return soup;
