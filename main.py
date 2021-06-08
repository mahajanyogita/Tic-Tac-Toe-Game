import board_formation
import insert_inboard
import check_winner
print("Lets Play TIC TAC TOE!\n")

while True:
    player1 = input("Enter Player 1 NAME: ")
    char1 = input("Enter character You Want (O/X) : ")
    player2 = input("Enter Player 2 Name: ")
    if char1 == 'X':
        char2 = 'O'
    else:
        char2 = 'X'

    players={char1: player1, char2: player2}

    print("\nPLAYER 1: ", player1, "YOU WILL USE CHARACTER", char1)
    print("\nPLAYER 2: ", player2, "YOU WILL USE CHARACTER", char2)

    playBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
            }

    board_char = board_formation.print_board(playBoard)
    max_count = 9
    match = 3
    while board_char.count(char1)+board_char.count(char2) < max_count:
        #for player1
        p1 = insert_inboard.Insert(player1, char1, playBoard)
        playBoard = p1.game()
        board_char = board_formation.print_board(playBoard)
        if board_char.count(char1) >= match:
            win = check_winner.winner(playBoard, char1)
            if win[0]:
                break
        if board_char.count(char1)+board_char.count(char2) == max_count:
            break
        #for player2
        p2=insert_inboard.Insert(player2, char2, playBoard)
        playBoard = p2.game()
        board_formation.print_board(playBoard)
        if board_char.count(char2) >= match:
            win = check_winner.winner(playBoard, char2)
            if win[0]:
                break

    if win[0]:
        print("Congratulations!", players[win[1]], "\nYOU ARE THE WINNER")
    else:
        print("GAME OVER ! Tie")

    again=input("\nWant to Play AGAIN?\t Press 'Y'\nTo Quit \t\t\t press 'N'\n")
    if again == 'N':
        print("THANK YOU!")
        break






