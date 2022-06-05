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
                print('the number you entered is too low, please try again: ')
            elif user_guess > number: 
                print('the number you guessed is too high, please try again: ')