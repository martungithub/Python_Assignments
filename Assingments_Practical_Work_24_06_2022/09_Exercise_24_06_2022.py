import random


def random_passwd(n):
    rand_passwd = ""
    ticket_numbers = random.sample(range(33, 127), n)
    for i in ticket_numbers:
        rand_passwd += chr(i)
    return rand_passwd


length = 0
while length < 1:
    length = int(input("Insert the password length: "))
print(random_passwd(length))
