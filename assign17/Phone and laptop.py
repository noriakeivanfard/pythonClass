import sqlite3

conn = sqlite3.connect('mydata.db')

c = conn.cursor()


c.execute("""
    CREATE TABLE customers (
        brand TEXT,
        name TEXT,
        year TEXT,
        camera TEXT,
        ram TEXT,
        memory TEXT,
        price TEXT
    )
""") 

c.execute("INSERT INTO customers VALUES('Samsung', 'A21s', '2020', '1080p', '6GB RAM', '128GB', '20')")

many_customers = [('Samsung', 'Galaxy Fold 5', '2023', '720p', '12GB RAM',  '256/512GB', '50'), 
                  ('Nokia', 'Redmi 12 5G', '2023', '1080p', '8GB RAM', '256GB', '16'), 
                  ('Samsung', 'Galaxy A5', '2017', '1080p', '3GB RAM', '32GB', '15'),
                  ('Iphone', 'iPhone 14 Plus', '2022', '120p', '6GB RAM', '512GB', '40'),
                  ('Iphone', 'iPhone 14 Pro Max', '2022', '1080p', '6GB RAM', '512GB', '59'),
                  ('Iphone', 'iPhone 13 mini', '2021', '1080p', '4GB RAM', '512GB', '50'),
                  ('Iphone', 'iPhone 11 Pro', '2019', '1080p', '4GB RAM', '512GB', '45'),
                  ('Samsung', 'Galaxy A54', '2023', '1080p', '8GB RAM', '256GB', '19'),
                  ('Samsung','Galaxy A14', '2023', '1080p', '6GB RAM', '128GB', '10')]
c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", many_customers)

c.execute("SELECT * FROM customers")

u_itame = c.fetchmany(2)

c.execute("SELECT * FROM customers WHERE year LIKE  '%2020'")

itames = c.fetchall()

for i in itames:
    print(i)

c.execute("UPDATE customers SET brand = 'Xiaomi' WHERE brand = 'Nokia'")

c.execute("SELECT * FROM customers")

itames = c.fetchall()
for i in itames:
    print(i)

itames = c.fetchall()
for i in itames:
    print(i)

c.execute("DROP TABLE customers")

itames = c.fetchall()
for i in itames:
    print(i)

conn.commit()

conn.close() 
