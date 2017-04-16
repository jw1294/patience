import patience
import os

def main():
    # Start the game
    os.system('clear') # clear screen: this will be removed
    game = patience.init_game()
    playing = True
    print 'Game Started!'
    print game

    # Game main loop
    while playing:
        move = raw_input('Enter your move: ')
        if move == 'd':
            result = game.deal()
        elif move == 'm':
            col_from = int(input('move from which colomn: '))
            col_to = int(input('move to which colomn: '))
            number = int(input('move how many: '))
            result = game.move_card(col_from, col_to, number)
        else:
            result = 1

        os.system('clear') # clear screen: this will be removed
        if result == 1:
            print 'Move Rejected!'
        else:
            print 'Move Accepted!'
        print game

if __name__ == '__main__':
    main()
