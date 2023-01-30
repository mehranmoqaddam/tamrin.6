import pyfiglet

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)
game = True
def show():
    for row in gameboard:
        for cell in row:
            print(cell," ", end="")
        print()

def check_game():
    for row in range(0, 3):
        if gameboard[row][0] == gameboard[row][1] == gameboard[row][2] == "X":
            print("player 1 wins")
            game = False
        elif gameboard[row][0] == gameboard[row][1] == gameboard[row][2] == "O":
            print("player 2 wins")
            game = False
    for col in range(0, 3):
        if gameboard[0][col] == gameboard[1][col] == gameboard[2][col] == "X":
            print("player 1 wins")
            game = False
        elif gameboard[0][col] == gameboard[1][col] == gameboard[2][col] == "O":
            print("player 2 wins")
            game = False
    if gameboard[0][0] == gameboard[1][1] == gameboard[2][2] or\
            gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == "X":
        print("player 1 wins")
    elif gameboard[0][0] == gameboard[1][1] == gameboard[2][2] or\
            gameboard[0][2] == gameboard[1][1] == gameboard[2][0] == "O":
        print("player 2 wins")
    if gameboard[0][0] != "-" and gameboard[0][1] != "-" and gameboard[0][2] != "-" and\
        gameboard[1][0] != "-" and gameboard[1][1] != "-" and gameboard[1][2] != "-" and\
        gameboard[2][0] != "-" and gameboard[2][1] != "-" and gameboard[2][2] != "-":
        print("it's draw")
        game = False
gameboard = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
show()
while game:
#player1

    print("Player 1")
    while True:
        row = int(input("satr : "))
        cell = int(input("sutun : "))
        if 0 <= row <= 2 and 0 <= cell <= 2:
            if gameboard[row][cell] == "-":
                gameboard[row][cell] = "X"
                show()
                check_game()
                break
            else:
                print("ye khune dge")
        else:
            print("beyne 0 va 2 vared kon")
#player2

    print("Player 2")
    while True:
        row = int(input("satr : "))
        cell = int(input("sutun : "))
        if 0 <= row <= 2 and 0 <= cell <= 2:
            if gameboard[row][cell] == "-":
                gameboard[row][cell] = "O"
                show()
                check_game()
                break
            else:
                print("ye khune dge")
        else:
            print("beyne 0 va 2 vare kon")
