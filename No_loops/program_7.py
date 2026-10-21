
# Write a program to check whether a character is a vowel or consonant.
vowel= ("a", "e", "i", "o", "u")
letter=input("Enter a letter: ")
if letter in vowel:
    print("Letter is a vowel")
else:
    print("Letter is a consonant")