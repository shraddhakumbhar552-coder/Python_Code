# Write a program to check whether a password is valid using nested if.
password = input("Enter a password: ")

# if len(password) >= 8:
#     if password == "shraddha123":
#         print("Password is valid")
#     else:
#         print("Password is invalid")
# else:
#     print("Password must contain at least 8 characters") 

if len(password) >= 8:
    if password.isalnum():
        print("Password is valid")
    else:
        print("Password is invalid. It should contain only letters and numbers.")
else:
    print("Password must contain at least 8 characters")