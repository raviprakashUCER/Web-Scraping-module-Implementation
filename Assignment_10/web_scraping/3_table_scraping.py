import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")

for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        data = [col.text.strip() for col in cols]
        if data:
            print(data)