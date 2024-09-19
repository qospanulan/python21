
# student_a = {
#     'name': 'Kaisar',
#     'age': '24'
# }
# print(student_a['age'])


students = [
    {'name': 'Kaisar', 'age': '24'},
    {'name': 'Oman', 'age': '19'},
    {'name': 'Vadim', 'age': '22'}
]

print(students[2])

for key, value in students[2].items():
    print(key, value)

