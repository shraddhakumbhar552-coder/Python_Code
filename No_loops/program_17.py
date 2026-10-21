
# Write a program to check grade based on marks (A, B, C, Fail).

marks=int(input("Enter your marks: "))
if marks>=90:
    print("You have scored A grade")
elif marks>=75:
    print("You have scored B grade")
elif marks>=55:
    print("You have scored C grade")
else:
    print("You failed the exam")