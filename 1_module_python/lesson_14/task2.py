# Количество каждого слова

text = (
    "Тихий ветер тихо дует, "
    "тихо шуршат листья под тихими шагами. "
    "В этой тишине тихо падают тени от деревьев, "
    "и тихая вода тихо колышется на озере. "
    "Всё вокруг кажется тихим и спокойным, "
    "как будто время замедлило свой тихий бег.")

# print(text)
text = text.lower()
words = text.split(" ")

for i in range(len(words)):
    words[i] = words[i].strip(",.")
# print(words)

words_cnt = {}

for slovo in words:
    words_cnt[slovo] = words_cnt.get(slovo, 0) + 1

print(words_cnt)

# for slovo in words:
#     if slovo not in words_cnt.keys():
#         words_cnt[slovo] = 1
#     else:
#         words_cnt[slovo] = words_cnt[slovo] + 1


# words_cnt["как"] = 1
# words_cnt["как"] = words_cnt["как"] + 1
# print(words_cnt)

# for slovo, kolvo in words_cnt.items():  # [(key, value), ()]
#     if kolvo > 1:
#         print(slovo, kolvo)
