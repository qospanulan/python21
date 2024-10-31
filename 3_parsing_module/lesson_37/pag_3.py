
data = [
    {"title": "title1", "description": ""},
    {"title": "title2", "description": ""},
    {"title": "title3", "description": ""},
    {"title": "title4", "description": ""},
    {"title": "title5", "description": ""},
    {"title": "title6", "description": ""},
    {"title": "title7", "description": ""},
    {"title": "title8", "description": ""},
    {"title": "title9", "description": ""},
    {"title": "title10", "description": ""},
]


offset = 0
limit = 3

for page in range(1, 10):
    print(f"\n== page {page} ==============================")

    offset = (page-1) * limit

    data_for_page = data[offset: offset + limit]
    for card in data_for_page:
        print(card)







