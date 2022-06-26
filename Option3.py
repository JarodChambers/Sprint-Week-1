#defining the function
def Option3():
    #importhing datetime
    import datetime as DT
    #getting the employees first name
    EmpFirst = input("what is the employees first name").title()
    #getting the employees last name
    EmpLast = input("what is the employees last name").title()
    #a loop to verify and collect the phone number
    while True:
        EmpPhone = input("what is the customers 10 digit phone number")
        if (len(EmpPhone)) == 10:
            break
        else:
            print("please try again, incorrect format")
    #getting the current date
    CurDate = DT.datetime.now()
    #getting the employees startdate and verifying it is in the correct form
    while True:
        try:
            StartDate = input("what is the employee startdate? (YYYY-MM-DD)")
            StartDate = DT.datetime.strptime(StartDate, "%Y-%m-%d")
            break
        except:
            print("date must be in the form YYYY-MM-DD")
    # getting the employees birthdate and verifying it is in the correct form
    while True:
        try:
            EmpBirth = input("what is the employees Birthdate? (YYYY-MM-DD)")
            EmpBirth = DT.datetime.strptime(EmpBirth, "%Y-%m-%d")
            break
        except:
            print("date must be in the form YYYY-MM-DD")
    #a blank line for spaceing
    print("")
    #printing the employees inital and last name
    print(f"{EmpFirst[0]}.{EmpLast}")
    #getting the employees age in days and printing it
    AgeDays =(CurDate-EmpBirth).days
    print(f"the employee is {AgeDays} Days old")
    #if the current date is in the past it prints how many days ago the employee statrted
    if CurDate > StartDate:
        StartedWorking = (CurDate - StartDate).days
        print(f"the employee started working {StartedWorking} days ago")
    # if the start date is in the future it prints how many days ntil the employee starts
    if CurDate < StartDate:
        NotStartedWorking = (StartDate - CurDate).days
        print(f"the employee started working {NotStartedWorking} days ago")
    # prints the employees current age in days
    AgeDays = (CurDate - EmpBirth).days
    #prints the employees phone number
    print(f"the employees phone number is {EmpPhone}")