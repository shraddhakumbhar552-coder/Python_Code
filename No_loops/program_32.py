# Write a program to check whether a student is eligible for an exam (attendance + marks).

attendance=int(input("Enter your attendance percentage: "))
marks=int(input("Enter your marks percentage: "))
if attendance>=75 and marks>=40:
    print("You are eligible to appear for the exam.")
else:
    print("You are not eligible to appear for the exam.")
