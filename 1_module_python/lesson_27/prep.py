import pandas as pd

data = {
    'Bob': ['I liked it.', 'It was awful.'],
    'Sue': ['Pretty good.', 'Bland.']
}

df = pd.DataFrame(data)
df.to_excel("test_data.xlsx", index=False)
