import pandas as pd

df = pd.read_csv('data/sales.csv')

df['total_price'] = df['Quantity'] * df['Price']

# print(df)

# print("== 1 ==============================")
# result = df.groupby('Product')[['total_price']].sum()
# print(result)

# print("== 2 ==============================")
# result = df[['total_price']].sum()
# print(result)

print("== 3 ==============================")
df['month'] = df['Date'].str[:7]

result = df.groupby('month')[['total_price']].sum()

print(result)
