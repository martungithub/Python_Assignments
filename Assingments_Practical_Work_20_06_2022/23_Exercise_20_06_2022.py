months = {
    "January": 31, "February": 29, "March": 31, "April": 30, "May": 31,
    "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
    "November": 30, "December": 31
}
month = input("Insert the month: ")
day = int(input("Insert the day: "))
if month == "March" or month == "April" or month == "May" and 1 <= day <= months[month]:
    print("Spring")
elif month == "June" or month == "July" or month == "August" and 1 <= day <= months[month]:
    print("Summer")
elif month == "September" or month == "October" or month == "November" and 1 <= day <= months[month]:
    print("Autumn")
elif month == "December" or month == "January" or month == "February" and 1 <= day <= months[month]:
    print("Winter")
else:
    print("Please input a valid information")
