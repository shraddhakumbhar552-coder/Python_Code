# Write a program to print grade description using match case.

grade=input("Enter your grade(A, B, C, D, F): ")
match grade:
    case "A":
        print(" your performance is Excellent")
    case "B":
        print(" your performance is Good")  
    case "C":
        print(" your performance is Average")
    case "D":
        print(" your performance is Below Average")
    case "F":
        print(" your performance is Fail")
    case _:
        print("Invalid grade")