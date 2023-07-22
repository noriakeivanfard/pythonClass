def date(day, month, year):
    day = int(input("day: "))
    month = int(input("month: "))
    year = int(input("year: "))
    return f"{year}/{month}/{day}"

print(date(1,2,3))
