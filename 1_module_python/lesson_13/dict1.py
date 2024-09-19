
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

cnt = 0
for friend in friends:
    print("friend", friend)
    if friend["age"] > 20:
        cnt = cnt + 1
        friend["больше 20 лет"] = True
    else:
        friend["больше 20 лет"] = False

print(cnt)
print(friends)
