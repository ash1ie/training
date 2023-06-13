import random
print('Welcome!')
name = input('What is your name? ') #Save user's name

def guess_the_number():
    number=random.randint(1,100) #Generate random number between 1 to 100
    guess = int(input('Guess a number between 1 and 100: ')) #saves first guess 
    tries = 1 #By default user has tried 1 time
    while guess != number: #Continuously asks user to guess until they get it right
        tries += 1 #counts how many tries it takes for user to get it
        if guess > number and guess <= 100:
            guess = int(input('Guess is too HIGH, try again: '))
        elif guess < number and guess >= 1: 
            guess = int(input('Guess is too LOW, try again: '))
        else: 
            guess = int(input('Invalid guess, try again: '))
    print('Congratulations! You guessed the number correctly!')
    print('You used:',tries,'guesses!')

guess_the_number()