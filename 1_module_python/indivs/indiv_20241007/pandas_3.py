import pandas as pd

df = pd.read_csv('./data/sales.csv')

# result = df.groupby('Product')['Quantity'].sum()

result = df.groupby('Product').agg(
    {
        'Quantity': 'sum',
        'OrderID': 'count'
    }
)

print(result)







