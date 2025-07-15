import sqlite3
import pandas as pd

conn = sqlite3.connect('scripts/data/youtube_data.db')
df = pd.read_sql_query("SELECT * FROM channel_stats", conn)
print(df)
conn.close()



# import sqlite3
# import pandas as pd

# conn = sqlite3.connect('data/youtube_data.db')  # ✅ Match exactly where your script saved the DB

# df = pd.read_sql_query("SELECT * FROM channel_stats", conn)
# print(df)

# conn.close()




# import sqlite3

# conn = sqlite3.connect('scripts/data/youtube_data.db')  # ✅ use your correct path here
# cursor = conn.cursor()

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# print("📋 Tables in your database:")
# for table in tables:
#     print("-", table[0])

# conn.close()
