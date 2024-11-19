from faker import Faker
import psycopg2
import random
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="internat11",
    database="python21_sql_4"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE new_users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        role_name VARCHAR(50),
        created_at TIMESTAMP
    );
""")

role_names = ['admin', 'moderator', 'web_app_user', 'guest']

for _ in range(100):

    role_name = random.choice(role_names)

    username = fake.user_name()
    email = fake.email()
    created_at = fake.date_time_this_decade(before_now=True, after_now=False)

    cursor.execute("""
        INSERT INTO new_users (username, email, created_at, role_name)
        VALUES (%s, %s, %s, %s);
    """, (username, email, created_at, role_name))

conn.commit()
cursor.close()
conn.close()

