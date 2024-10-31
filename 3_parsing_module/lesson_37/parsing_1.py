import requests
from bs4 import BeautifulSoup
# "https://stopgame.ru/game_compilations"

custom_headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

response = requests.get('https://quotes.toscrape.com/page/1/', headers=custom_headers)

soup = BeautifulSoup(
    markup=response.text,
    features="html.parser"
)

elements = soup.find_all("div", attrs={'class': 'quote'})

for elem in elements:
    quote = elem.find("span", attrs={'class': 'text'})
    print(f"Quote: {quote.text}")
    author = elem.find("small", attrs={'class': 'author'})
    print(f"Author: {author.text}")
    tags = elem.find_all("a", attrs={'class': 'tag'})

    tags_text = []
    for tag in tags:
        tags_text.append(tag.text)

    print(f"Tags: {', '.join(tags_text)}")

    print("\n================================================\n")

