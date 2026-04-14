import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://example.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = {
    "title": [soup.title.text],
    "paragraph": [soup.p.text]
}

# ✅ ALWAYS use absolute safe path
output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, "data.csv")

df = pd.DataFrame(data)
df.to_csv(file_path, index=False)

print("CSV saved successfully at:", file_path)