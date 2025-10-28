import os

#Your job is to fix some variable names, clean up the 'winner' function and add some whitespace and comments. 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show(spot):
    for r in range(3):
        print(f" {spot[r * 3]} | {spot[r * 3 + 1]} | {spot[r * 3 + 2]} ")
        if r < 2:
            print("---+---+---") #print row separator

def winner(spot):
    # X winning configs
    if spot[0] == 'X' and spot[1] == 'X' and spot[2] == 'X':
        return 'X'
    if spot[3] == 'X' and spot[4] == 'X' and spot[5] == 'X':
        return 'X'
    if spot[6] == 'X' and spot[7] == 'X' and spot[8] == 'X':
        return 'X'
    if spot[0] == 'X' and spot[3] == 'X' and spot[6] == 'X':
        return 'X'
    if spot[1] == 'X' and spot[4] == 'X' and spot[7] == 'X':
        return 'X'
    if spot[2] == 'X' and spot[5] == 'X' and spot[8] == 'X':
        return 'X'
    if spot[0] == 'X' and spot[4] == 'X' and spot[8] == 'X':
        return 'X'
    if spot[2] == 'X' and spot[4] == 'X' and spot[6] == 'X':
        return 'X'

    # O winning configs
    if spot[0] == 'O' and spot[1] == 'O' and spot[2] == 'O':
        return 'O'
    if spot[3] == 'O' and spot[4] == 'O' and spot[5] == 'O':
        return 'O'
    if spot[6] == 'O' and spot[7] == 'O' and spot[8] == 'O':
        return 'O'
    if spot[0] == 'O' and spot[3] == 'O' and spot[6] == 'O':
        return 'O'
    if spot[1] == 'O' and spot[4] == 'O' and spot[7] == 'O':
        return 'O'
    if spot[2] == 'O' and spot[5] == 'O' and spot[8] == 'O':
        return 'O'
    if spot[0] == 'O' and spot[4] == 'O' and spot[8] == 'O':
        return 'O'
    if spot[2] == 'O' and spot[4] == 'O' and spot[6] == 'O':
        return 'O'
    return None


def play():
    spot = [str(i) for i in range(9)]
    turn = "X"
    while any(cell.isdigit() for cell in spot):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(spot)
        print(f"\n{turn}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if 0 <= move < 9 and spot[move].isdigit():
            spot[move] = turn
            winner_result = winner(spot) #check win configs
            if winner_result:
                clear_screen()
                print("Tic-Tac-Toe\n")
                show(spot)
                print(f"\n{winner_result} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Spot is taken or out of range. Try again.")
    clear_screen() #clean up spotefore final message

    print("Tic-Tac-Toe\n")
    
    show(spot)
    
    print("\nIt's a draw!")

play()
