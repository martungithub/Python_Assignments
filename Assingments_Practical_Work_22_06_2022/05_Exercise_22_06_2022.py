def palindrome(string):
    string = string.lower()
    res = ""
    for ch in string:
        if ch.isalpha() or ch == " ":
            res += ch
    new_list = res.split(" ")
    if new_list == new_list[::-1]:
        return True
    else:
        return False

string = input("Insert the string: ")
print(palindrome(string))
