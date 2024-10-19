import requests

response = requests.get('https://quotes.toscrape.com/')

data = response.text

# '“', '”'

pre_quotes = data.split('“')[1:]

for pre_quote in pre_quotes:
    # print(pre_quote)
    quote = pre_quote.split('”')[0]
    print(f'Quote: {quote}')
    print('\n\n================================\n\n')


