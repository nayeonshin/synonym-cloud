import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.thesaurus.com/"


def _get_synonyms(url: str) -> list:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    synonym_container = soup.find("div", {"id": "meanings"})
    lis = synonym_container.find_all("li")

    synonyms = []
    for li in lis:
        synonyms.append(li.text)

    return synonyms


def get_synonyms() -> list:
    search_term = input("Search: ").lower()
    search_url = f"{BASE_URL}browse/{search_term}"
    synonyms = _get_synonyms(search_url)
    return synonyms


if __name__ == "__main__":
    get_synonyms()
