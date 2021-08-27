# user will guess the number
import random

def user_guess(end_number):
    random_number = random.randint(1,end_number)
    guess = 0
    while guess != random_number:
        guess= int(input("Enter the number between 1 and " + str(end_number) + " to make a guessing range: "))
        if guess>random_number:
            print("Sorry! your guess is to high")
        elif guess<random_number:
            print("Sorry! your guess is to small")

    print("Congrats! you have guessed the correct number which is " + str(random_number))

user_guess(20)

#computer will guess the number

def Computer_guess(end_number):
    low = 1
    high= end_number
    user_feedback=''
    while user_feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        user_feedback= input("Is the number " +str(guess) + " is to high(h), too low(l) or is it correct(c): " )
        if user_feedback== 'h':
            high = guess -1
        elif user_feedback == 'l':
            low = guess + 1

    print("Congrats! you have guessed the correct number.")

Computer_guess(20)