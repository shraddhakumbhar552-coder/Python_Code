# Write a program to check the type of number (single, double, or three digit).

num=int(input("Enter a number: "))
if num>=0 and num<=9:
    print("It is a single digit number")
elif num>=10 and num<=99:
    print("It is a two digit number")
elif num>=100 and num<=999:
    print("It is a three digit number")
else:   
    print("It is not a single, two or three digit number")