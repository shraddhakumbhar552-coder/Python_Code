
# Write a program to check whether a number is positive and even using nested if.
num=int(input("Enter a number: "))
if num>=0:
    print("The number is positive")
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative")