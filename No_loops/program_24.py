# Write a program to check exam results (Distinction, First Class, Pass, Fail).
marks=int(input("Enter your marks: "))
if marks>=75:
    print("You have passed with Distinction.")
elif marks>=60:
    print("You have passed with First Class.")
elif marks>=40:
    print("You have passed.")
else:
    print("You have failed.")
