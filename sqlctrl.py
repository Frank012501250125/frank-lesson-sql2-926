import sqlite3

#INSERT
sqlins = """
INSERT INTO "main"."product_info" ("name", "version", "remark") 
VALUES ('123', '456', '789');
"""
conn = sqlite3.connect('DevOps.db')
cursor = conn.cursor()
cursor.execute('SELECT * From product_info;')
records = cursor.fetchall()
print (records)