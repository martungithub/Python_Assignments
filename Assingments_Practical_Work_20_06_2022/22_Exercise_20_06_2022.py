vowels = ['a', 'e', 'i', 'o', 'u']
vowel = input("Insert a letter: ")
if vowel.isupper():
    vowel = vowel.lower()
if vowel == 'y':
    print("y both a vowel and consonant")
else:
    for i in vowels:
        if i == vowel:
            print(vowel, "is a vowel")
