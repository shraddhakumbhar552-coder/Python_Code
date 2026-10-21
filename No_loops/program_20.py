# Write a program to check ticket price based on age.
age=int(input("Enter your age: "))
if age<5:
    print("Ticket price is free")
elif age>=5 and age<=12:
    print("Ticket price is rs100")
elif age>=13 and age<=60:
    print("Ticket price is rs200")
else:
    print("Ticket price is rs150")