
# . Write a program to print month days using match case.
month = int(input("Enter the month (1-12): "))
match month:
    case 1:
        print("January has 31 days")
    case 2:
        print("February has 28 days")
    case 3:
        print("March has 31 days")
    case 4:
        print("April has 30 days")
    case 5:
        print("May has 31 days")
    case 6:
        print("June has 30 days")
    case 7:
        print("July has 31 days")
    case 8:
        print("August has 31 days")
    case 9:
        print("September has 30 days")
    case 10:
        print("October has 31 days")
    case 11:
        print("November has 30 days")
    case 12:
        print("December has 31 days")
    case _:
        print("Invalid month")