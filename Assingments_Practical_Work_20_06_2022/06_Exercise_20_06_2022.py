order = float(input("Insert amount of order: "))
tip = order * 18 / 100
tax = order * 20 / 100
pay = order * 18 / 100 + order * 20 / 100 + order
print("Tip:", tip, "\nTax:", tax, "\nTotal:", format(pay, ".2f"))
