# Defining function

def claimtotal():
    Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    MonthTot = []
    LoopNums = 0
    while LoopNums < 12:
        MonthInputs = int(input(f"please enter the total for {Months[(LoopNums)]}: "))
        MonthTot.append(MonthInputs)
        # print(MonthInputs)
        LoopNums = LoopNums + 1

    sum_result = sum(MonthTot)
    print("Yearly claims total: ")
    print(sum_result)