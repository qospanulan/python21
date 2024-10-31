import requests
from bs4 import BeautifulSoup


for page_num in range(1, 11):
    print(f"\n== page number {page_num} =========================================\n")
    response = requests.get(f'https://quotes.toscrape.com/page/{page_num}/')

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

