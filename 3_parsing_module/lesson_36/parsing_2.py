import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

elements = soup.find_all("span", attrs={'class': 'text'})

for elem in elements:
    print(elem.text)
    print("\n================================================\n")




