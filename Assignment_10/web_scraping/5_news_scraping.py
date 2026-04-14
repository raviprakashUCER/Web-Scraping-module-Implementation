import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

print("NEWS HEADLINES:\n")

for t in titles:
    print(t.text)