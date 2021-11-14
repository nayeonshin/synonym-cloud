import requests
from bs4 import BeautifulSoup

BASE_URL = "https://scholar.google.com/"


def _get_result_num(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    result = soup.find("div", {"id": "gs_ab_md"}).text.split()
    return result[1]


def get_result_nums(synonyms):
    result_nums = []
    for synonym in synonyms:
        search_url = f"{BASE_URL}scholar?hl=en&q={synonym}"
        _get_result_num(search_url)
