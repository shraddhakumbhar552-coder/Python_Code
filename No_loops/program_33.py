# Write a program to check whether a person can apply for a loan.

age=int(input("Enter your age: "))
income=int(input("Enter your income: "))
if age>=21 and income>=25000:
    print("You are eligible to apply for a loan.")  
else:
    print("You are not eligible to apply for a loan.")