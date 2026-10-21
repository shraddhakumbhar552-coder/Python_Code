# Write a program to check whether a number is divisible by both 3 and 7 or not.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print("First number is the greatest")   

elif num2>num1 and num2>num3:
    print("Second number is the greatest")
    
else:
    print("Third number is the greatest")