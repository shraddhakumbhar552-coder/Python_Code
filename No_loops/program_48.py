# Write a program to print language choice using match case.
language = input("Enter your language choice (Python, Java, C++, JavaScript): ").capitalize()
match language:
    case "Python":
        print("You have chosen Python")
    case "Java":
        print("You have chosen Java")
    case "C++":
        print("You have chosen C++")
    case "JavaScript":
        print("You have chosen JavaScript")
    case _:
        print("Invalid language choice")
        
        