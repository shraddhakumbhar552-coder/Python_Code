# Write a program to calculate electricity bill based on units consumed.
units=int(input("Enter number of units consumed: "))
if units<=100:
    bill=units*5
    print("Your electricity bill is:",bill)
elif units<=200:
    bill=100*5+(units-100)*7
    print("Your electricity bill is:",bill)
else:
    bill=100*5+100*7+(units-200)*10
    print("Your electricity bill is:",bill)
