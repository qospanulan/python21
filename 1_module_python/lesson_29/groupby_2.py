import pandas as pd

data = {
    "A": [1, 3, 99],
    "B": [4, 2, 5]
}

df = pd.DataFrame(data)
print(df)
print("================================================")
df['result'] = df['A'] + df['B']

print(df)




