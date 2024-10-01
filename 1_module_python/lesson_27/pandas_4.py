import pandas as pd

file_path = "people.csv"
df = pd.read_csv(file_path)
print("== df ==============================")
print(df)


df_filtered = df[df['City'] == 'Dallas']
print("\n== df_filtered ==============================")
print(df_filtered)
