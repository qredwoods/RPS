# simple game of rock paper scissors in the commandline
import random
import time
WELCOME_MESSAGE = 'Welcome to rock paper scissors'
RULES = ""
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

REPLAY_QUERY = 'Rematch? enter (Y)es to play again... ' 


def main(): 
    print(WELCOME_MESSAGE)
    print(RULES)
    playing = True
    player = input('What is your name? ')
    options = [ROCK, PAPER, SCISSORS]
    count = 1
    while playing:
        computer_choice = random.choice(options)
        player_choice = input("Type to choose: Rock, Paper, or Scissors? ").casefold()
        
        # add validation to ensure the answer is precisely rock, paper, or scissors, or to correct spelling mistakes
        # could also for user ease have it just be 'r' 'p' or 's' for input
        victor = ''
        
        # determine winner
        if computer_choice == player_choice:
            end_game = "It's a tie!"
        elif player_choice == 'rock':
            if computer_choice == PAPER:
                victor = "computer"
            elif computer_choice == SCISSORS:
                victor = player
        elif player_choice == 'scissors':
            if computer_choice == ROCK:
                victor = 'computer'
            elif computer_choice == PAPER:
                victor = player
        elif player_choice == 'paper':
            if computer_choice == SCISSORS:
                victor = 'computer'
            elif computer_choice == ROCK:
                victor = player

        if victor:
            end_game = f'{victor} Won!'
        
        player_choice = player_choice.capitalize()
        computer_choice = computer_choice.capitalize()

        print(f'ROUND {count}')
        print(f'{player} vs. computer')
        print(f'{player_choice} vs. {computer_choice}')
        
        if victor == player:
            print(f'{player_choice} beats {computer_choice}!')
        elif victor == 'computer':
            print(f'{computer_choice} beats {player_choice}!')
        
        print(end_game)
        replay_ans = input(REPLAY_QUERY)
        if replay_ans in ['y', 'Y', 'yes', 'Yes']:
            count += 1
            continue
        quit()
        
    
        
        


        
        



if __name__=="__main__":
    main()