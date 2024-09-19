friends = [
    {
        "name": "Adil",
        "age": 23,
        "first_meet_year": 2019
    },
    {
        "name": "Tamara",
        "age": 27,
        "first_meet_year": 2023
    },
    {
        "name": "Rustem",
        "age": 17,
        "first_meet_year": 2015
    }
]

CURRENT_YEAR = 2024

for friend in friends:
    years = CURRENT_YEAR - friend["first_meet_year"]

    if years > 2:
        print(friend)














