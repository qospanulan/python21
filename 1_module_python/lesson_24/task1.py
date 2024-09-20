# Есть файл text.txt с текстом. Надо найти все
# слова с буквой "з" и заменить эти слова на "***".
# Результат прописать в файл output1.txt.


with open("./text.txt") as file:
    data = file.read()

print(data)

words = data.split(" ")
new_data = []

for word in words:
    if 'з' in word or 'З' in word:
        new_data.append("***")
    else:
        new_data.append(word)

# print(new_data)
new_data = " ".join(new_data)
print(new_data)

with open("./output1.txt", 'w') as file:
    file.write(new_data)




