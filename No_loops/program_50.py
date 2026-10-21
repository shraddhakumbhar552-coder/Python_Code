
# Write a program to build a simple ATM menu using a match case.
atm_menu = input("Enter your choice (E for Exit, W for Withdraw, D for Deposit): ").upper()
match atm_menu:
    case "E":
        print("Exiting...")
    case "W":
        print("Withdrawing money...")
    case "D":
        print("Depositing money...")
    case _:
        print("Invalid choice")