#defining the function
import datetime as DT
def Option1():
    while True:
        # collecting the employee number and verying that it is 5 digits
        EmpNum = input("what is the employee number(must be 5 characters type End to quit)").title()
        if EmpNum == "End":
            break
        while len(EmpNum) != 5:
            EmpNum = input("Invalid syntax please enter the 5 digit employee number").title()
        # collecting the employee first name and verifying that it is not blank
        EmpFirstName = input("what is the employees first name").title()
        while len(EmpFirstName) == 0:
            EmpFirstName = input("Invalid syntax name cannot be blank please enter name again").title()
        # collecting the employee last name and verifying that it is not blank
        EmpLastName = input("what is the employees last name").title()
        while len(EmpLastName) == 0:
            EmpLastName = input("Invalid syntax name cannot be blank please enter name again").title()
        # collecting the location of the trip
        Location = input("what is the location of the trip")
        # collecting the start date
        while True:
            try:
                StartDate = input("what is the start date? (YY-MM-DD)")
                StartDate = DT.datetime.strptime(StartDate, "%y-%m-%d")
                break
            except:
                print("date must be in the form YY-MM-DD")
        # collecting the end date
        while True:
            try:
                EndDate = input("what is the end date? (YY-MM-DD)")
                EndDate = DT.datetime.strptime(EndDate, "%y-%m-%d")
                (EndDate - StartDate).days < 7
                EndDate > StartDate

                break
            except:
                print(
                    "date must be in the form YY-MM-DD, must be less than 7 days from start date and be after the start date")
        # calculating the number of days
        NumDays = (EndDate - StartDate).days
        # checking to see wieather the car is owned or rented
        while True:
            Car = input("is the car owned or rented, please enter O for owned and R for rented").upper()
            if Car == "O" or "R":
                break
        # checlkign to see if the kilometers exceed 2000
        while True:
            Kilometers = int(input("how many kilometers are you traveling(cannot exceed 2000)"))
            if Kilometers <= 2000:
                break
        # checking if it is excutive or standard
        while True:
            Claim = input("please enter the claim type S for standard and E for executive").upper()
            if Claim == "E" or "S":
                break
        # calculating per diem
        PerDiem = NumDays * 85
        # calculating mileage
        if Car == "O":
            Mileage = Kilometers * .17

        if Car == "R":
            Mileage = NumDays * 65
        # Bonus calculations
        Bonus = 0
        if NumDays > 3:
            Bonus = Bonus + 100
        if Kilometers > 1000 and Car == "O":
            Bonus = Bonus + (Kilometers * .04)
        if Claim == "E":
            Bonus = Bonus + (NumDays * 45)
        if StartDate.month == 12:
            if 15 < StartDate.day < 22:
                Bonus = Bonus + (NumDays * 50)
        ClaimAmmount = PerDiem + Mileage + Bonus
        ClaimTotal = ClaimAmmount * 1.15

        # formating values for the print statements
        PerDiemStr = f"${PerDiem:,.2f}"
        MileageStr = f"${Mileage:,.2f}"
        BonusStr = f"${Bonus:,.2f}"
        ClaimAmmountStr = f"${ClaimAmmount:,.2f}"
        ClaimTotalStr = f"${ClaimTotal:,.2f}"

        # printing all the inputs and values
        print("")
        print(f"the employees number is {EmpNum}")
        print(f"the employees name is {EmpFirstName} {EmpLastName}")
        print(f"the location of the trip is {Location}")
        print(f"the trip is from {StartDate} to {EndDate} and lasts {NumDays} days")
        if Car == "O":
            print(f"the car is owned")
            print(f"the milage is {MileageStr}")
        if Car == "R":
            print(f"the car is a rental")
            print(f"the rental allowance is {MileageStr}")
        print(f"the perdiem is {PerDiemStr}")
        print(f"the bonus is {BonusStr}")
        print(f"the claim ammount is {ClaimAmmountStr}")
        print(f"the claim total is {ClaimTotalStr}")
        print("Please press any key to continue...")