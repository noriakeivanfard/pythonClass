import datetime
today = datetime.datetime.today()
today_year = (today.year)
day = int(input("enter day : "))
month = int(input("enter month: "))
year = int(input("enter year : "))

age = today_year - year

print(f"You {age} years old ")

day = age * 365
week = age * 52       
second = age * 31536000

print(f" weeks:{week} \n days:{day} \n seconds:{second} ")
