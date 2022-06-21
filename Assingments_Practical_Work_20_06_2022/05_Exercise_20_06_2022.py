under_1_bottles = float(input("How many under 1L bottles do you have?: "))
more_than_1_bottles = int(input("How many more than 1L bottles do you have?: "))
cash = under_1_bottles * 0.10 + more_than_1_bottles * 0.25

print("You have: $", format(cash, ".2f"), "cash")
