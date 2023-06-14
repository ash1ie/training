import random

print('Welcome!')
name = input('What is your name? ') #Save user's name

def guess_the_number(): 
    number=random.randint(1,100) #Generate random number between 1 to 100
    print(number)
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

    highscores_text = open("highscores.txt", "a")
    highscores_text.write(name + ': ' + str(tries) + '\n') #saves the current user and new score to file
    highscores_text.close()

    menu()

def highscores(): #open the highscores
    scores = {} #creates dictionary

    with open('highscores.txt','r') as f: #adds lines to dictionary
        for line in f.readlines():
            scores[line.split(':')[0].strip()] = int(line.split(':')[1].strip())
    scores = sorted(scores.items(), key=lambda x:x[1], reverse=False) #sorts scores from lowest to highest
    
    top_ten = scores[:10]
    for key, value in top_ten: 
        print("%s\t%s" % (key, value))
    
    menu()

def end_game(): #end program
    print('Goodbye, '+name)
    exit()

def menu():
    print('Menu: \n1) Play game\n2) Highscores\n3) Quit')
    inp_choice = input('What would you like to do? ')
    if inp_choice == '1':
        guess_the_number()
    elif inp_choice == '2':
        highscores()
    elif inp_choice == '3':
        end_game()
    else:
        print('Invalid choice.')

menu()