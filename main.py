# Imports for functions

import Option1
import Option2
import Option3
import Option4

# Main Menu
while True:
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim")
    print("2. Fun Interview Question")
    print("3. Cool Stuff with Strings and Dates")
    print("4. Graph Monthly Claim Totals")
    print("5. Quit Program")

    #verifying that the number is between 1 and 5
    Choice = int(input("Enter choice: (1-5): "))
    while Choice > 5 or Choice < 1:
        Choice = int(input("please enter an number between 1 and 5"))

    # Choices
    if Choice == 1:
        Option1.Option1()
    elif Choice == 2:
        Option2.option2()
    elif Choice == 3:
        Option3.Option3()
    elif Choice == 4:
        Option4.linegraph()
    elif Choice == 5:
        quit()