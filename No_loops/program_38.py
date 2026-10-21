# Write a program to check whether a student passed all subjects.
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 35 and science >= 35 and english >= 35:
    print("Student passed all subjects")
else:
    print("Student failed")