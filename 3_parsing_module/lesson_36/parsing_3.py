import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

elements = soup.find_all("div", attrs={'class': 'quote'})

for elem in elements:
    quote = elem.find("span", attrs={'class': 'text'})
    print(quote.text)
    print("\n================================================\n")

