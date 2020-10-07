import sqlite3
import pandas as pd
conn = sqlite3.connect('data/technicalDebtDataset.db')

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

#df = pd.read_sql_query("SELECT * FROM table_name", conn)