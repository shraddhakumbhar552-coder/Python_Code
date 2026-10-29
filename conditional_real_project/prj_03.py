
        
# ATM Withdrawal System
from colorama import Fore, Back, Style, init
init()

acc_holder_name = input("Enter Account Holder Name: ").strip().title()

if acc_holder_name == '':
    print("Holder name cannot be empty")

else:
    current_balance = input("Enter your current balance: ").strip()

    if current_balance.isdigit():
        current_balance = int(current_balance)

        withdrawal_amount = input("Enter your withdrawal amount: ").strip()

        if withdrawal_amount.isdigit():
            withdrawal_amount = int(withdrawal_amount)

            # Transaction logic
            transaction_status = ""
            remaining_bal = current_balance

            if withdrawal_amount <= 0:
                transaction_status = Fore.RED+"Amount must be greater than zero"

            elif withdrawal_amount > 20000:
                transaction_status = Fore.RED+"Maximum withdrawal allowed is ₹20,000"

            elif withdrawal_amount > current_balance:
                transaction_status = Fore.RED+"Insufficient balance"

            else:
                transaction_status = "Withdrawal Successful"
                remaining_bal = current_balance - withdrawal_amount

            # Final transaction details
            print("\n========== ATM TRANSACTION DETAILS ==========")
            print("Account Holder Name:", acc_holder_name)
            print("Current Balance: ₹", current_balance)
            print("Withdrawal Amount: ₹", withdrawal_amount)
            print("Transaction Status:", transaction_status)

            if transaction_status == "Withdrawal Successful":
                print("Remaining Balance: ₹", remaining_bal)

                if remaining_bal < 1000:
                    print("Low Balance Warning")

        else:
            print("Enter a valid withdrawal amount")

    else:
        print(Fore.RED + "Enter a valid current balance")