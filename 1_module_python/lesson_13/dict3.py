
d = {
    "adil": ["math", "geometry", "history"],
    "rustem": ["math"],
    "tamara": ["geometry", "history", "math"]
}

max_cnt = -1
max_student = ""

for student, subjects in d.items():  # d.items() => [ ("adil", [...]), ("rustem", [...]), ("tamara", [...])]
    # print(student, " | ", subjects)

    cnt = len(subjects)
    if cnt > max_cnt:
        max_cnt = cnt
        max_student = student

print(max_student, "|", max_cnt)



