import sqlite3

sql = "SELECT * FROM Lotto"

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()  # 查詢全部
for row in rows:
    print(row)

conn.close()