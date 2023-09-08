'''solo attempt at wordle'''

import colorama

from colorama import Fore

word = 'stars'
def turn():
    playing = True
    guess = input(Fore.WHITE+'Guess: ')
    i = 0
    output = ''

    for letter in word:
        # checks if the first letter of the guess matches the first letter of the correct word
        if letter == guess[i]:
            output += Fore.GREEN + guess[i]

        # checks if the first letter of the guess is correct, but in the wrong place (NOT WORKING :()
        if letter in guess and letter != guess[i]:
            output += Fore.YELLOW + guess[i]
        
        if letter not in guess:
            output += Fore.RED + guess[i]
        i += 1
    
    print(output)

    if guess == word:
        print(Fore.GREEN+"you win!")
        playing = False
        exit()
    
    return playing

turn()

'''
def game():
    playing = True
    num_turns = 0
    playing = turn()
    while playing == True:
        num_turns += 1
        playing = turn()
        if num_turns >= 6:
            playing = False
            print(Fore.RED+'Game over!')

game()
'''
'''
for turn in range(5):
    print(turn())
    if turn() == False:
        exit()
        '''
'''
i = 0
for letter in word:
    print(letter)
    print(guess[i])
    if guess[i] == letter:
        #print(letter + '!')
        print()
    else:
       # print(letter)
       print()
    i += 1
'''