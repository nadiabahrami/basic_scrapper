"""Scrapper part1."""
from bs4 import BeautifulSoup
import io
import sys
import requests


INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': 'Seattle',
    'Zip_Code': '98101',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'B'
}


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    resp = requests.get(url, params=params)
    resp.raise_for_status() # <- This is a no-op if there is no HTTP error
    # remember, in requests `content` is bytes and `text` is unicode
    return resp.content, resp.encoding


def write_file(content, name):
    file = open(name, "w")
    file.write(content)


def load_inspection_page(name, **kwargs):
    content, encoding = get_inspection_page(**kwargs)
    write_file(content.decode(encoding), name)
    file = io.open(name, "r")
    return file


def parse_source(html):
    parsed = BeautifulSoup(html, 'html5lib')
    return parsed


if __name__ == '__main__':
    kwargs = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98109'
    }
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html = load_inspection_page('inspection_page.html', **kwargs)
    else:
        html, encoding = get_inspection_page(**kwargs)
    doc = parse_source(html)
    print(doc.prettify())

# soup = BeautifulSoup(html_doc, 'html.parser')
