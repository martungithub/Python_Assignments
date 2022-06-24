word = input("Insert the word: ")
new_word = ""
for i in range(len(word) - 1, -1, -1):
    new_word += word[i]
print("Reversed: ", new_word)
