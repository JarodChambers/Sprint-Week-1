def misc():
    #the phrase that you want to replace all the vowels in
    say = input("what is the saying")
    #the letter you want to replace all the vowels with
    letter = input("what letter would you like to replace the vowel with")
    #the commands to replace the vowels with the selected letter
    say = say.replace("a",letter)
    say = say.replace("e",letter)
    say = say.replace("i",letter)
    say = say.replace("o",letter)
    say = say.replace("u",letter)
    #printing the output saying
    print(say)