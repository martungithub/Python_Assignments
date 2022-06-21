investment = float(input("Insert the amount of your investment: "))
first_year = investment + investment * 4 / 100
second_year = first_year + first_year * 4 / 100
third_year = second_year + second_year * 4 / 100
print("First year: ", first_year, "\nSecond year: ", second_year, "\nThird year: ", third_year)
