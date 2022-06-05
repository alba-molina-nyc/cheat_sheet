"""
write a function (guessing_game) that takes no arguments
when run the function chooses a random integer between 0 and 100

then ask the user to guess what number has been chosen

each time the user enters a guess the program indicates if the guess is 
1. too high
2. too low
3. or guessed correctly 

if the person guesses correctly then exit the program 

otherwise the user is asked to guess again

-- import random in order to use random method to generate the random number
"""
import random 

def guess_the_num():
    number = random.randint(1,15) 

    while True: 
        user_guess = int(input('please enter a number between 0 and 100: '))
        if user_guess == number:
            print('correct!')
            break
        else:
            if user_guess < number:
                too_low = "the number you entered is too low, please try again" 
                print(too_low)
                continue
            elif user_guess > number: 
                too_high = "the number you guessed is too high, please try again"
                print(too_high)
                continue


guess_the_num()



"""
while True: 
    is an infinite loop so it is important to set break points when you need to exit the loop so that you are not stuch in an infinite loop because it will break your program"""
# continue
# break
# return 
# pass


"""


TODO: ask what if we do not pass continue?

def guess_the_num():
    number = random.randint(1,15) 

    while True: 
        user_guess = int(input('please enter a number between 0 and 100: '))
        if user_guess == number:
            print('correct!')
            break
        else:
            if user_guess < number:
                too_low = "the number you entered is too low, please try again" 
                print(too_low)
                continue
            elif user_guess > number: 
                too_high = "the number you guessed is too high, please try again"
                print(too_high)
                continue"""