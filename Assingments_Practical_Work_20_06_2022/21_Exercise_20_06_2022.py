months = {
    "January": 31, "February": [28, 29], "March": 31, "April": 30, "May": 31,
    "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
    "November": 30, "December": 31
}
month = input("Insert the month: ")
for i in months.keys():
    if i == month:
        print(months[month])
