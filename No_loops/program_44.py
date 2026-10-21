# . Write a program to check traffic signal actions using match case.
signals=input("Enter the signals (red, yellow, green): ")
match signals:
    case "red":
        print("Stop")
    case "yellow":
        print("Prepare to stop")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")
        