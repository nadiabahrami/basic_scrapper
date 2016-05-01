"""Scrapper part1."""
from bs4 import BeautifulSoup
import requests
import io
import sys


# INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
# INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
# INSPECTION_PARAMS = {
#     'Output': 'W',
#     'Business_Name': '',
#     'Business_Address': '',
#     'Longitude': '',
#     'Latitude': '',
#     'City': 'Seattle',
#     'Zip_Code': '98101',
#     'Inspection_Type': 'All',
#     'Inspection_Start': '',
#     'Inspection_End': '',
#     'Inspection_Closed_Business': 'A',
#     'Violation_Points': '',
#     'Violation_Red_Points': '',
#     'Violation_Descr': '',
#     'Fuzzy_Search': 'N',
#     'Sort': 'B'
# }

def get_inspection_page(parameters_go_here):
