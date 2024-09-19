
l = ["hello", "world", "justcode", "apple", "oranget"]
# l = ["h", "t", "f", "a", "p"]

n = len(l)

commons_max_count = -1
index1 = None
index2 = None

for i in range(n):
    print("внешний цикл", l[i])
    for j in range(i + 1, n):
        # if i == j:
        #     continue
        print(l[i], "x", l[j])
        set1 = set(l[i])
        set2 = set(l[j])
        commons = set1.intersection(set2)

        print("общие буквы", len(commons))
        if commons_max_count < len(commons):
            commons_max_count = len(commons)
            index1 = i
            index2 = j

    print("================================")

print("maximum:", commons_max_count)
print("strs:", l[index1], l[index2])
# print("strs:", index1, index2)










# text = ("В глубине леса, где деревья тянутся к небу, как гигантские колонны, "
#         "скрывается маленькое озеро, окружённое мягким мхом и папоротниками. "
#         "На поверхности воды играют солнечные блики, создавая волшебные узоры, "
#         "а тихий шёпот ветра наполняет воздух спокойствием. "
#         "Здесь, вдали от суеты и шума, можно забыть о времени и просто наслаждаться красотой природы.")
