import random
#A game where you have to guess 4 different digits with the correct number AND position

#Ensure user inputs are 2, 3, or 4 digits and only numbers are allowed
def isXDigits(number, total):
    
    if len(number) != total:
        return False
    
    zeroToNine = "0123456789"
    for x in number :
        if x not in zeroToNine:
            return False
    return True
    
def guessNumberPlay(numberOfDigits):
    #Rules of the game
    print("This game is to guess the correct "+str(numberOfDigits)+" random digits number")
    print("x Bingo!, y Other digit(s) correct but wrong position!")
    print("There are total x numbers with correct position and correct number")
    print("There are total y numbers with wrong position but correct number")
    #numberOfDigits = int(input("Please enter the number of digits to start the game : "))
    
    # to generate 4 digits number with all different numbers
    rannumber = ""                                          #create empty string for reference
    for x in range(numberOfDigits) :                        #conditional statement to run for how many times based on user input(age)
        onenumber = str(random.randint(0, 9))               #generate one random number

        #===========================Enable this line to generate different number for each one========================================
        #while onenumber in rannumber:                      #check whether generated number is the same with referenced
        #    onenumber = str(random.randint(0, 9))          #if true then generate another random number until condition satisfied
        #=============================================================================================================================
        
        rannumber = rannumber + onenumber                   #store generated number in referenced number

    #print("This is the answer " + rannumber)
    fournumber = input("Enter a number with "+ str(numberOfDigits) +" digits to play the game : ")
    while isXDigits(fournumber, numberOfDigits) == False:                #call function to check whether input is legit 4 digit number
        fournumber = input(fournumber+" is not "+ str(numberOfDigits) +" digits number. Please key in again : ")
    
    numOfGuess = 1                                          #initialize guessed count by 1
    guesscorrect = False                                    #set guess flag to false for first time run
    while guesscorrect == False:                            #run the commands while the guess flag is false until true
        samepos = 0                                         #set same position check variable to 0
        diffpos = 0   
        sameList = []
        rannumberList = list(rannumber)
        fournumberList = list(fournumber)
        for x in range(numberOfDigits):           #for loop to run the command below 4 times
            if fournumberList[x] == rannumberList[x]:              #check generated number is the same with user input at position x
                samepos += 1   
                fournumberList[x] = "A"
                rannumberList[x] = "A"
                sameList.append(x)   
        for x in range(numberOfDigits):           #for loop to run the command below 4 times
            if x in sameList:
                continue
            if fournumberList[x] in rannumberList:  
                index = rannumberList.index(fournumberList[x])
                fournumberList[x] = "B"
                rannumberList[index] = "B"
                diffpos += 1    
        print(str(samepos)+" BINGO!, " + str(diffpos)+" Other digit(s) correct but wrong position!")
        if(samepos == numberOfDigits):                                   #condition for if all guessed number is correct
            guesscorrect = True                             #set guess flag to true
            print("CONGRATULATIONS! BRAVO! You guess the number correctly : "+rannumber + " in " + str(numOfGuess) + " attempt(s)")
        else:                                               
            if numOfGuess % 5 == 0:
                endTheGame = input("Do you want to end the game since you have tried "+str(numOfGuess)+" times, (Y or N)")
                if(endTheGame in ['Y', 'y']):
                    print("Thanks for playing.")
                    print("Here's the answer for your session - " + rannumber)
                    exit();

            fournumber = input("Try again : ")
            while isXDigits(fournumber, numberOfDigits) == False:
                fournumber = input(fournumber+" is not "+ str(numberOfDigits) + " digits number. Please keyin again : ")
            numOfGuess += 1


#Combination of Room 1 and Room 2 scripts
print("Salam and Good Afternoon" )
print("We are from Room 1" )
ageInput = int(input("Please key in an age, from 0 to 99:  "))
while ageInput > 99 or ageInput < 0:
    ageInput = int(input("Please key in an age, from 0 to 99:  "))
numberOfDigit = 0 
if ageInput >= 0 and ageInput <= 14:
    numberOfDigit = 2 
elif ageInput >= 15 and ageInput <= 64:
    numberOfDigit = 4
elif ageInput >= 65 and ageInput <=99:
    numberOfDigit = 3


guessNumberPlay(numberOfDigit)