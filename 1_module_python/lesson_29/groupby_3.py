import pandas as pd

df = pd.read_csv('data/sales.csv')

print(df)
print("================================================")
del df['Category']

print(df)


