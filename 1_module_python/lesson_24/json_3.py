
import json

# file = open("./json_test.json", "r")
#
# data = file.read()
#
# file.close()

with open("./json_test.json", "r") as file:
    data = file.read()


print(type(data))
print(data)
print("================================")

parsed_data = json.loads(data)
print(type(parsed_data))
print(parsed_data)
print(parsed_data['name'])
print(parsed_data['email'])




