# Write a program to check whether a year is a leap year and century year.
year=int(input("Enter your year: "))
if year%400==0:
    print("It is a leap and century year")
elif year%100==0:
    print("It is a century year but not a leap year")
elif year%4==0:
    print("It is a leap year but not a century year")
else:
    print("It is not a leap year and not a century year")

    