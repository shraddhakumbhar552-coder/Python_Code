
# Mini Project 5: Salary Bonus Calculator

from colorama import Fore, Back, Style, init
init(autoreset=True)

# Employee Details
emp_name = input(Fore.CYAN + "Enter Employee Name: ").strip().title()

if emp_name == "":
    print(Fore.RED + "Employee name cannot be empty")

else:
    monthly_salary = input(Fore.CYAN + "Enter Monthly Salary: ").strip()
    experience = input(Fore.CYAN + "Enter Years of Experience: ").strip()
    rating = input(Fore.CYAN + "Enter Performance Rating (1-5): ").strip()

    # Input Validation
    if monthly_salary == "" or experience == "" or rating == "":
        print(Fore.RED + "All fields are compulsory")

    elif monthly_salary.isdigit() and experience.isdigit() and rating.isdigit():

        monthly_salary = int(monthly_salary)
        experience = int(experience)
        rating = int(rating)

        # Rating Validation
        if rating < 1 or rating > 5:
            print(Fore.RED + "Invalid Rating! Enter rating between 1 and 5")

        elif monthly_salary <= 0:
            print(Fore.RED + "Monthly salary must be greater than zero")

        else:
            # Bonus Calculation
            if experience >= 10 and rating >= 4:
                bonus_percentage = 20

            elif experience >= 5 and rating >= 4:
                bonus_percentage = 15

            elif experience >= 2 and rating >= 3:
                bonus_percentage = 10

            else:
                bonus_percentage = 0

            # Bonus Amount Calculation
            bonus_amount = monthly_salary * bonus_percentage / 100
            final_salary = monthly_salary + bonus_amount

            # Performance Message
            if rating == 5:
                performance_message = "Excellent Performer"
            elif rating >= 3:
                performance_message = "Good Performer"
            else:
                performance_message = "Needs Improvement"

            # Final Output
            print(Fore.YELLOW + "\n========== EMPLOYEE BONUS DETAILS ==========")
            print(Fore.CYAN + "Employee Name:", Fore.WHITE + emp_name)
            print(Fore.CYAN + "Monthly Salary: ₹", Fore.WHITE + str(monthly_salary))
            print(Fore.CYAN + "Years of Experience:", Fore.WHITE + str(experience))
            print(Fore.CYAN + "Performance Rating:", Fore.WHITE + str(rating))
            print(Fore.GREEN + "Bonus Percentage:", str(bonus_percentage) + "%")
            print(Fore.GREEN + "Bonus Amount: ₹", bonus_amount)
            print(Fore.GREEN + "Final Salary: ₹", final_salary)
            print(Fore.MAGENTA + "Performance Message:", performance_message)

    else:
        print(Fore.RED + "Please enter valid numeric values")
