import pandas as pd

data = {
    "column_1": [13, 27, 32, 99],
    "column_2": ['a', 'b', 'c', 'd']
}

df = pd.DataFrame(data)
df.set_index('column_1', inplace=True, drop=False)

print(df)
print("\n== loc ===============================")
print(df.loc[32])

print("\n== loc[:] ===============================")
print(df.loc[13:32])

print("\n== iloc ==============================")
print(df.iloc[3])

print("\n== iloc[:] ==============================")
print(df.iloc[0:2])

