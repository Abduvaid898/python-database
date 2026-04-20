# from fordb import connect
# ulash=connect()
# cur = ulash.cursor()
# ulash.autocommit = True

# cur.execute(
#     "CREATE DATABASE shop"
# )
# print("😂")

# cur.execute(
#     """CREATE TABLE products(
#     id SERIAL PRIMARY KEY,
#     brend VARCHAR(100),
#     madel VARCHAR(100),
#     price NUMERIC(10 ,2)
#     )"""
# )
# print("🤣")

# cur.execute(
#     "INSERT INTO products(brend ,madel ,price) VALUES('artel' ,'muzlatgich' ,10000000) ,('artel' ,'changyutgich' ,1000000) ,('samsung' ,'S26' ,16000000) ,('samsung' ,'A56' ,5000000)"
# )
# print("🤣")

# cur.execute(
#     "SELECT * FROM products"
# )
# print("🤣")

# cur.execute(
#     "SELECT SUM(price) FROM products"
# )
# cur.execute(
#     "SELECT AVG(price) FROM products"
# )
# cur.execute(
#     "SELECT MIN(price) FROM products"
# )
# cur.execute(
#     "SELECT MAX(price) FROM products"
# )
# cur.execute(
#     "SELECT COUNT(price) FROM products"
# )
# cur.execute(
#     "SELECT * FROM products WHERE brand IN ('samsung')"
# )
# cur.execute(
#     "SELECT * FROM products WHERE brand NOT IN ('samsung')"
# )
# rows=cur.fetchall()
# for row in rows:
#     print(row)