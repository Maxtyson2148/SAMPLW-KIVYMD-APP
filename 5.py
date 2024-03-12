import random

print('''                    GAME

            ROCK PAPER SCISSORS\n''')
print('''                 GAME RULES\n
  1. ALWAYS USE CAPITAL LETTERS FOR INPUT
  2. NUMERIC CHARECTORS ARE BOT ALLOWED FOR       INPUT
  3. ANY KIND OF SYMBOLS ARE NOT ALLOWED\n\n''')
def game():              
    player_move=input(' Pick a move between ROCK, PAPER, SCISSORS :\n\n      ')
   
    print('Game Output ⬇️\n')
    print('player: \n\n', player_move,'\n\n')

    computer_move = random.randint(1,3)

    if computer_move==1:
        print('Computer: \n\n','ROCK\n')
        if player_move == 'ROCK':
            print('\n   Draw, try again!\n\n')
            game()
        if player_move == 'PAPER':
            print('\n   YOU WON!\n\n')
            game()
        if player_move == 'SCISSORS':
            print('\n   YOU LOST!\n\n')
            game()    
                
    if computer_move==2:
        print('Computer: \n\n','PAPER\n')
        if player_move == 'PAPER':
            print('\n   Draw, try again!\n\n')
            game()
        if player_move == 'SCISSORS':
            print('\n   YOU WON!\n\n')
            game()
        if player_move == 'ROCK':
            print('\n   YOU LOST!\n\n')
            game()     
                    
    if computer_move==3:
        print('Computer: \n\n','SCISSORS\n')
        if player_move == 'SCISSORS':
            print('\n   Draw, try again!\n\n')
            game()
        if player_move == 'ROCK':
            print('\n   YOU WON!\n\n')
            game()
        if player_move == 'PAPER':
            print('\n   YOU LOST!\n\n')
            game()    
game()
