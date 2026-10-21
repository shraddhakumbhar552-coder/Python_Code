# 19. Write a program to print the day name based on day number (1–7).
day_num=int(input("Enter day number (1-7): "))
if day_num==1:
    print("Monday")
elif day_num==2:
    print("Tuesday")    
elif day_num==3:
    print("Wednesday")
elif day_num==4:
    print("Thursday")
elif day_num==5:
    print("Friday")
elif day_num==6:
    print("Saturday")
elif day_num==7:
    print("Sunday")
else:
    print("Invalid day number. Please enter a number between 1 and 7.")
    