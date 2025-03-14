from helper import draw_board, check_turn
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9',}

playing = True
turn = 0

while playing:
    #Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #Get input from player
    choice = input()
    if choice =='q':
        playing = False
        #Check if the player gave a spot from 1-9
    elif str. isdigit(choice) and int(choice) in spots:
        #checks i the spot given is already taken
        if not spots[int(choice)] in {'X', "O"}:
            #Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)