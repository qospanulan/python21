import pandas as pd

df = pd.read_csv('./data/sales.csv')

# print(df)

df_electronics = df[df['Category'] == 'Electronics']
df_appliances = df[df['Category'] == 'Appliances']

# print(df_electronics)
# print(df_appliances)

df_electronics.to_csv('./data/sales_electronics.csv')
df_appliances.to_csv('./data/sales_appliances.csv')


