import pandas as pd

df = pd.read_csv('data/sales.csv')


# print("== 1 ==============================")
# result = df.groupby('Category')[['Price']].mean()
# print(result)

print(df.columns.values)

print("== 2 ==============================")
result = df.groupby('Category').agg(
    {
        'Price': ['max', 'min', 'mean', 'sum'],
        'Quantity': 'sum',
        'Date': ['min', 'max']
    }
)

# print( type(result['Price']) )
# print( result['Price']['max'] )

print(result.columns.values)

result.columns = ['_'.join(col) for col in result.columns.values]
print(result.columns.values)
print(result)


