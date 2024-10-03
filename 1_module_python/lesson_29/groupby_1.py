import pandas as pd

df = pd.read_csv('data/sales.csv')

# print(df)

result = df.groupby('Product')[['Quantity']].sum()

print(result)
