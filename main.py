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
            result = game.move_cards(col_from, col_to, number)
        elif move == 'r':
            col_to = int(input('move to which colomn: '))
            result = game.raise_card(col_to)
        elif move == 'f':
            col_to = int(input('which colomn to flip: '))
            result = game.flip(col_to)
        elif move == 's':
            col_from = int(input('which colomn to stack: '))
            stack_to = int(input('which stack: '))
            result = game.stack_card(col_from, stack_to)
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
