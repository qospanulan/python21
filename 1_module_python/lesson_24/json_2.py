import json

data = {
    "date": "19.09.2024",
    "time": "20:22"
}


file = open("json_test_2.json", "w", encoding="utf-8")


json_data = json.dumps(data)
file.write(json_data)
print(type(json_data))
print(json_data)

# json.dump(data, file)

file.close()
