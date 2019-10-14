import numpy as np
def start():
    return [["","",""],["","",""],["","",""]]

def print_Grad(g):
    for i in range(3):
        print(g[i])

def player_Turn(g,a):
    while True:
        x = int(input("enter x"))
        y = int(input("enter y"))
        if grad[x-1][y-1] == '':
            grad[x - 1][y - 1]=a
            break
        else :
            print("can't")
    return g

def computer_Trun(g,a):
    while True:
        x = np.random.randint(1, 4)
        y = np.random.randint(1, 4)
        if grad[x-1][y-1] == '':
            grad[x - 1][y - 1]=a
            break
    return g

def check_Win(g):
    for row in range(0,3):
        if grad[row][0] == grad[row][1] and grad[row][0] == grad[row][2] and grad[row][0] != '':
            return grad[row][0]
        if grad[0][row] == grad[1][row] and grad[0][row] == grad[2][row] and grad[0][row] != '':
            return grad[0][row]
    if grad[0][0] == grad[1][1]  and grad[0][0] == grad[2][2] and grad[0][0] != '':
        return grad[0][0]
    if grad[0][2] == grad[1][1] and grad[0][2] == grad[2][0] and grad[0][2] != '':
        return grad[0][2]

    return -1


print("welcome in Tic Tak Tok Game")
print("---------------------------")
x = np.random.randint(1,4)


fin = False
while fin == False:
    grad = start()
    print("1 player / 2 players")
    type_Of_Game = int(input("number of palyers"))
    if type_Of_Game == 1:
        player_Name = input("player name")
        flage = False
        for i in range(0,9):
            ans = check_Win(grad)
            if ans == 'x':
                print(player_Name +  "win")
                flage = True
                break
            elif ans == 'o':
                print("computer win")
                flage = True
                break
            if i%2 == 0:
                grad = player_Turn(grad,'x')
                print_Grad(grad)
            else:
                grad = computer_Trun(grad, 'o')
                print_Grad(grad)
        if flage == False:
            ans = check_Win(grad)
            if ans == 'x':
                print("player 1 win")
            elif ans == 'o':
                print("computer win")
            else:
                print("Draw")
    elif type_Of_Game == 2:
        player_1_Name = input("player 1 name")
        player_2_Name = input("player 2 name")
        flage = False
        for i in range(0, 9):
            ans = check_Win(grad)
            if ans == 'x':
                print(player_1_Name + " win")
                flage = True
                break
            elif ans == 'o':
                print(player_2_Name + " win")
                flage = True
                break
            if i % 2 == 0:
                grad = player_Turn(grad, 'x')
                print_Grad(grad)
            else:
                grad = player_Turn(grad, 'o')
                print_Grad(grad)
        if flage == False:
            ans = check_Win(grad)
            if ans == 'x':
                print("player 1 win")
            elif ans == 'o':
                print("computer win")
            else:
                print("Draw")

    cont = input("want to play again or no (yes/on)")
    if cont == 'no':
        fin = True























