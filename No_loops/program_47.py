# Write a program to check user role (admin, user, guest) using match case.

role = input("Enter your role (admin, user, guest): ")
match role:
    case "admin":
        print("You have full access")
    case "user":
        print("You have limited access")
    case "guest":
        print("You have guest access")
    case _:
        print("Invalid role")
    