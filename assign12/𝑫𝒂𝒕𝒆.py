def date(day, month, year):
    day = int(input("day: "))
    month = int(input("month: "))
    year = int(input("year: "))
    print(year, "/", month, "/", day, sep="")

print(date(1,2,3))
