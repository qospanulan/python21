import os

base_dir = "/home/qospanulan/edu/justcode/python21/1_module_python/lesson_30/spy_reports"
filenames = os.listdir(base_dir)

print(filenames)

for filename in filenames:
    filepath = f"{base_dir}/{filename}"
    print(filepath)
    with open(filepath, 'r') as f:
        data = f.read()
        print(data)

    print("\n================================================\n")
