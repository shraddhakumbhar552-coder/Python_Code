# Write a program to print menu-based food selection using match case.

# menu=input("Enter your menu(vegetarian, non-vegetarian, vegan, gluten-free): ")
# match menu:
#     case "vegetarian":
#         print("Your food is Paneer Butter Masala")
#     case "non-vegetarian":
#         print("Your food is Chicken Burger")
#     case "vegan":
#         print("Your food is Vegetable Pasta")
#     case "gluten-free":
#         print("Your food is Salad")
#     case _:
#         print("Invalid choice")
        
        
menu=input("Enter your choice(1-4): ")
match menu:
    case "1":
        print("Your food is Paneer Butter Masala")
    case "2":
        print("Your food is Chicken Burger")
    case "3":
        print("Your food is Vegetable Pasta")
    case "4":
        print("Your food is Salad")
    case _:
        print("Invalid choice")