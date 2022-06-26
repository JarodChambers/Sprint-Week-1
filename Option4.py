import matplotlib.pyplot as plt

# Function that creates a line graph for Monthly Claim Totals
def linegraph():
    Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    MonthTotal = []
    LoopNum = 0
    while LoopNum < 12:
        MonthInput = int(input(f"please enter the total for {Month[(LoopNum)]}: "))
        MonthTotal.append(MonthInput)
        # print(MonthInput)
        LoopNum = LoopNum + 1

    y_axis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    plt.plot(Month, MonthTotal)

    plt.xlabel("Months")

    plt.ylabel("Totals")

    plt.title("Monthly Claim Totals")

    plt.grid(True)

    plt.show()
    print()
# Display Message
    print("Press any key to continue...")