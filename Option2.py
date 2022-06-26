def option2():
    BuzzNum = 0
    while BuzzNum < 100:
        #Adds 1 to the number every loop
        BuzzNum = BuzzNum + 1
        #finds if the number is divisible by 8 and 5
        if BuzzNum % 8 == 0 and BuzzNum % 5 == 0:
            Word = "FizzBuzz"
        #finds if the number is divisible by 5
        elif BuzzNum % 5 == 0:
            Word = "Fizz"
        #finds if the number is divisible by 8
        elif BuzzNum % 8 == 0:
            Word = "Buzz"
        #makes the variable the number if it is not divisible by 8, 5 or both
        else:
            Word = (BuzzNum)
        #prints the word variable
        print(Word)
        print("Press any key to continue...")