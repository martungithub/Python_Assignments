days = int(input("Insert days: "))
hours = int(input("Insert hours: "))
minutes = int(input("Insert minutes: "))
seconds = int(input("Insert seconds: "))
answer = 86400 * days + 3600 * hours + 60 * minutes + seconds
print("Answer: ", answer)
