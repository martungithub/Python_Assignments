def days(year, month):
    months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
        6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    if int(year) % 4 == 0 and month == 2:
        return 29
    return months[month]


inp_year = input("Insert the year: ")
inp_month = 0
while inp_month not in range(1, 13):
    inp_month = int(input("Insert the month(1-12): "))

print(days(inp_year, inp_month))
