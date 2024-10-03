import pandas as pd

df = pd.read_csv('data/sales.csv')


def my_func(column):
    print(column)
    print("\n==========================\n")
    return column


# df['Category'] = df.apply(my_func, axis='columns')
df.apply(my_func, axis=1)

print(df)



