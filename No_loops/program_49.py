# Write a program to print result status using match case.
result = input("Enter result status (pass, fail, incomplete): ")
match result:
    case "pass":
        print("Congratulations! You have passed.")
    case "fail":
        print("Sorry! You have failed.")
    case "incomplete":
        print("Your result is incomplete. Please check again.")
    case _:
        print("Invalid result status")