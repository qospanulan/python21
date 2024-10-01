import pandas as pd

print("\n== users ========================================\n")

df_users = pd.read_csv("data/users.csv")
print(df_users.head(3))

print("\n== posts ========================================\n")

df_posts = pd.read_csv("data/posts.csv")
print(df_posts.head(3))

print("\n== result ========================================\n")
df_result = pd.merge(
    left=df_users,
    right=df_posts,
    on=['user_id']
)

print(df_result.head(3))
df_result.to_csv("data/result.csv", index=False)






























