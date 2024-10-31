
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

page = 1
page_size = 5

# page 1 -> [0:3]   [ page_size * (page-1) : page_size * page ]
# page 2 -> [3:6]
# page 3 -> [6:9]
# page 4 -> [9:12]


for page in range(1, 9):
    print(f"\n== page {page} ==============================")
    data_for_page = data[page_size * (page-1): page_size * page]
    for card in data_for_page:
        print(card)







