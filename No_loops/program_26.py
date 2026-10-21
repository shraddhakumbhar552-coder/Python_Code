# # . Write a program to check month names based on month number.
# month_number = int(input("Enter month number (1-12): "))
# if month_number == 1:
#     print("January")
# elif month_number == 2:
#     print("February")
# elif month_number == 3:
#     print("March")
# elif month_number == 4:
#     print("April")
# elif month_number == 5:
#     print("May")
# elif month_number == 6:
#     print("June")
# elif month_number == 7:
#     print("July")
# elif month_number == 8:
#     print("August")
# elif month_number == 9:
#     print("September")
# elif month_number == 10:
#     print("October")
# elif month_number == 11:
#     print("November")
# elif month_number == 12:
#     print("December")
# else:
#     print("Invalid month number. Please enter a number between 1 and 12.")

month = int(input("Enter month number (1-12): "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")