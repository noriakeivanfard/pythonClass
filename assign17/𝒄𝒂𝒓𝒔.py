import csv
import sqlite3

cars = [] 
with open("assign17/car.csv", "r") as file:
    a = csv.reader(file)
    b = next(a)
    for row in a:
        cars.append(tuple(row))

conne = sqlite3.connect("cars.db")
c = conne.cursor() 
c.execute("""
    CREATE TABLE cars (
            Car TEXT,
            MPG TEXT,
            Cylinders TEXT,
            Displacement TEXT,
            Horsepower TEXT,
            Weight TEXT,
            Acceleration TEXT,
            Model TEXT,
            Origin TEXT
    )
""")

c = conne.cursor() 
for i in range(len(cars)):
    c.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", cars[i])

def japan_cars():
    c.execute("SELECT * FROM cars WHERE Origin LIKE 'Japan%'")
    items = c.fetchall() 
    for item in items:
        print(item)
def longe_small():
    c.execute("SELECT * FROM cars ORDER BY Car DESC")
    item = c.fetchall()
    print(item[-1])
    c.execute("SELECT * FROM cars ORDER BY Car DESC")
    item = c.fetchall()
    print(item[0])
def Cylinders():
    car = 0
    c.execute('SELECT * FROM cars WHERE Cylinders')
    item = c.fetchall()
    for i in range(len(item)):
        car += int(item[i][2])
    x = float(car // len(item))
    print(x) 
def Horsepower():
    car = 0
    c.execute('SELECT * FROM cars WHERE Horsepower')
    item = c.fetchall()
    for i in range(len(item)):
        car += float(item[i][4])
    x = float(car // len(item))
    print(x)
def Light_cars():
    c.execute("SELECT name Weight FROM luxury_cars ORDER BY  Weight DECE LIMIT 50")
    items = c.fetchall()
    for item in items:
        print(item)
        
op=int(input("""
1_Show cars made in Japan
2_Which car name is long and which name car is short? 
3_Number of cylinders between cars?
4_What is the average horsepower of cars?
5_Say 50 light cars
which one?""")) 

if op == 1:
    japan_cars()
elif op == 2:
    longe_small()
elif op == 4:
    Cylinders()
elif op == 5:
    Horsepower()
elif op == 6:
    Light_cars()

conne.commit()
conne.close() 

