import random

def get_random_number():
    random_number = random.randint(0, 9)
    return random_number

def isNumber(number):
    zeroToNine = "0123456789"
    for x in number :
        if x not in zeroToNine:
            return False
    return True
    
print("===== Welcome to Number Guessing Game =====")
chances = 0
while 1:
    choice = input("Do you wanna play (y/n): ")
    if 'y' in choice.lower():
        print("Generating random number between 0 and 9")
        random_number = get_random_number()
        while 1:
            chances += 1
            #user_number = int(input("Enter the number you think it is: "))
            userkeyin = input("Enter the number you think it is: ")
            while isNumber(userkeyin) == False:
                chances += 1
                userkeyin = input("This is not number. Please enter again: ")
            user_number = int(userkeyin)    
            if user_number > 9 or user_number < 0:
                print("Invalid input...please try again")
            else:
                if user_number == random_number:
                    print("Conguratulation !!! You got the number in {0} chances\n".format(chances))
                    chances = 0
                    break
                elif user_number > random_number:
                    if abs(user_number - random_number) <= 4:
                        print("Close, try a lower number")
                    else:
                        print("Not even close, try a lower number")
                elif user_number < random_number:
                    if abs(user_number - random_number) <= 4:
                        print("Close, try a higher number")
                    else:
                        print("Not even close, try a higher number")
    elif 'n' in choice.lower():
        print("Exiting...")
        break
    else:
        print("Invalid input...please try again")
