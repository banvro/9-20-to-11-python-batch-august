import requests
from bs4 import BeautifulSoup as be

base_url = "https://www.latlong.net/"

# Headers to simulate a real browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

serching = "sector 1 gurgaon latitude & longitude"

html_code = requests.get(base_url + serching, headers=HEADERS)

# print(html_code.content)

soup = be(html_code.content, "html.parser")

target = soup.find("input", class_ = "lat")

print(target.text)