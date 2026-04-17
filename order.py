# import psycopg2
# def connect():
#     conn=psycopg2.connect(
#         host="localhost",
#         database="students",
#         user="postgres",
#         password="vorislar2026"
#     )
#     return conn

# from db import connect
# ulash=connect()
# cur = ulash.cursor()
# ulash.autocommit = True

# cur.execute(
#     "CREATE DATABASE students"
# )
# print("yaratildi")

# cur.execute(
#     """CREATE TABLE oquvchilar(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     score INTEGER
#     )"""
# )
# print("ok")

# cur.execute(
#     "INSERT INTO oquvchilar(name ,score) VALUES('Abdubaid' ,100) ,('Ixlosek' ,95) ,('Humoyun' ,90) ,('Golibjon' ,85) ,('Nizomiddin' ,80)"
# )
# print("qoshildi")

# cur.execute(
#     "INSERT INTO oquvchilar(name ,score) VALUES('HUMAYUN' ,60)"
# )

# cur.execute(
#     "SELECT * FROM oquvchilar WHERE name ILIKE 'H%' "
# )

# rows= cur.fetchall()
# for row in rows:
#     print(row)