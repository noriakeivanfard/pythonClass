import sqlite3

conn = sqlite3.connect('mydata.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE customers(
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

c.execute("SELECT * FROM customers WHERE year LIKE  '%2017'")

itames = c.fetchall()

for i in itames:
    print(i)
    
print('________________________________________________________________________________')
c.execute("UPDATE customers SET brand = 'Xiaomi' WHERE brand = 'Nokia'")

c.execute("SELECT * FROM customers")

itames = c.fetchall()
for i in itames:
    print(i)


c.execute("DROP TABLE customers")

itames = c.fetchall()
for i in itames:
    print(i)
    

print("_________________________________________________________________")
c.execute("""
    CREATE TABLE customers(
        brand TEXT,
        name TEXT,
        cpu TEXT,
        ram TEXT,
        sdd TEXT,
        os TEXT
    )
""") 
many_customers = [('Vivobook E410MA-BV1517', '14 inch Asus', '30',  '4GB RAM', '256GB', 'Windows'), 
                  ('Microsoft inches', '12.4 Microsoft inches', '50', '4GB RAM',  '64GB', 'Windows'), 
                  ('Vivobook R465EA-EB1592', '14.1 inch Asus', '30', '4GB RAM', '512GB', 'Windows'),
                  ('Legion 5 15IAH7H-i7 16GB 1SSD RTX 3060', '15 inch Lenovo', 'Core i7', '16GB RAM', '1 terabyte', 'Windows'),
                  ('Victus 15-FA0031DX', '15.6 Inch HP', '25', '8GB RAM', '512GB', 'Windows')]

c.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", many_customers) 

c.execute("SELECT * FROM customers")
itames = c.fetchall()

for i in itames:
    print(i)

c.execute("DELETE FROM customers WHERE cpu == '30'")

print("______________________________________________________________")
c.execute("SELECT * FROM media ORDER BY imdb DESC")
lap = c.fetchall()
for i in range(5):
    try:
        print(lap[i])
    except:
            pass
print("_________________________________________________________________")

conn.commit()

conn.close() 
