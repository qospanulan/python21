import pandas as pd

data = {
    "column_1": [13, 27, 32, 99],
    "column_2": ['a', 'b', 'c', 'd']
}

df = pd.DataFrame(data)

print(type(df))
print("================================")
print(type(df['column_1']))
print("================================")
print(df['column_1'])





