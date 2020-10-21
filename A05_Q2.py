board_a = [["0","1","2"],["3","4","5"],["6","7","8"]]
board_b = [["0","1","2"],["3","4","5"],["6","7","8"]]
board_c = [["0","1","2"],["3","4","5"],["6","7","8"]]
boards = [board_a,board_b,board_c]
alphabets = ["A","B","C"]
digits = ["0","1","2","3","4","5","6","7","8"]

def insertBoard(board,pos):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if pos == board[i][j]:
                board[i][j] = "X"

def print_board():
    print("      ".join(['{}'.format(item) for item in alphabets]))
    for i in range(3):
        for k in range(len(boards)):
            for j in range(3):
                if j == 2 and k != len(boards) - 1:
                    print(boards[k][i][j], end = "  ")
                elif j == 2 and k == len(boards) - 1:
                    print(boards[k][i][j], end = "")
                else:
                    print(boards[k][i][j], end = " ")
        print()

def isWinner(board,le):
    return ((board[0][0] == le and board[0][1] == le and board[0][2] == le) or
    (board[1][0] == le and board[1][1] == le and board[1][2] == le) or
    (board[2][0] == le and board[2][1] == le and board[2][2] == le) or
    (board[0][0] == le and board[1][0] == le and board[2][0] == le) or
    (board[0][1] == le and board[1][1] == le and board[2][1] == le) or
    (board[0][2] == le and board[1][2] == le and board[2][2] == le) or
    (board[0][0] == le and board[1][1] == le and board[2][2] == le) or
    (board[0][2] == le and board[1][1] == le and board[2][0] == le))

def removingBoard(k,board):
    if isWinner(board,"X"):
        alphabets.remove(k)
        boards.remove(board)

def knightsMove(board,player2):
    import copy
    copy = copy.deepcopy(board)

    if player2 == 0:
        if board[1][2] != "X":
            insertBoard(copy,"5")
            return 7 if isWinner(copy, "X") else 5
        elif board[2][1] != "X":
            insertBoard(copy,"7")
            return 5 if isWinner(copy, "X") else 7

    elif player2 == 1:
        if board[2][1] != "X":
            insertBoard(copy,"6")
            return 8 if isWinner(copy, "X") else 6
        elif board[2][2] != "X":
            insertBoard(copy,"8")
            return 6 if isWinner(copy, "X") else 8

    elif player2 == 2:
        if board[1][0] != "X":
            insertBoard(copy,"3")
            return 7 if isWinner(copy, "X") else 3
        elif board[2][1] != "X":
            insertBoard(copy,"7")
            return 3 if isWinner(copy, "X") else 7

    elif player2 == 3:
        if board[0][2] != "X":
            insertBoard(copy,"2")
            return 8 if isWinner(copy, "X") else 2
        elif board[2][2] != "X":
            insertBoard(copy,"8")
            return 2 if isWinner(copy, "X") else 8

    elif player2 == 5:
        if board[0][0] != "X":
            insertBoard(copy,"0")
            return 6 if isWinner(copy, "X") else 0
        elif board[2][0] != "X":
            insertBoard(copy,"6")
            return 0 if isWinner(copy, "X") else 6

    elif player2 == 6:
        if board[0][1] != "X":
            insertBoard(copy,"1")
            return 5 if isWinner(copy, "X") else 1
        elif board[1][2] != "X":
            insertBoard(copy,"5")
            return 1 if isWinner(copy, "X") else 5

    elif player2 == 7:
        if board[0][0] != "X":
            insertBoard(copy,"0")
            return 2 if isWinner(copy, "X") else 0
        elif board[0][2] != "X":
            insertBoard(copy,"2")
            return 0 if isWinner(copy, "X") else 2

    elif player2 == 8:
        if board[0][1] != "X":
            insertBoard(copy,"1")
            return 3 if isWinner(copy, "X") else 1
        elif board[1][0] != "X":
            insertBoard(copy,"3")
            return 1 if isWinner(copy, "X") else 3

def trap_2X(board):
    for i in digits:
        import copy
        copy = copy.deepcopy(board)
        move = i
        insertBoard(copy,move)
        if ((copy[0][0] == "X" and copy[1][2] == "X" and copy[2][1] == "X") or 
        (copy[0][1] == "X" and copy[1][2] == "X" and copy[2][0] == "X") or
        (copy[0][1] == "X" and copy[1][0] == "X" and copy[2][2] == "X") or
        (copy[0][2] == "X" and copy[1][0] == "X" and copy[2][1] == "X") ) and not isWinner(board,"X"):
            return move

def mirrorMove(board):
    import copy
    copy = copy.deepcopy(board)
    if board[1][1] != "X":
        if copy[0][0] == "X" and copy[2][2] != "X":
            return copy[2][2]
        elif copy[0][1] == "X" and copy[2][1] != "X":
            return copy[2][1]
        elif copy[0][2] == "X" and copy[2][0] != "X":
            return copy[2][0]
        elif copy[1][0] == "X" and copy[1][2] != "X":
            return copy[1][2]
        elif copy[1][2] == "X" and copy[1][0] != "X":
            return copy[1][0]
        elif copy[2][0] == "X" and copy[0][2] != "X":
            return copy[0][2]
        elif copy[2][1] == "X" and copy[0][1] != "X":
            return copy[0][1]
        elif copy[2][2] == "X" and copy[0][0] != "X":
            return copy[0][0]
    
def sacrifice(board):
    for i in digits:
        import copy
        copy = copy.deepcopy(board)
        move = i
        insertBoard(copy,i)
        if isWinner(copy,"X"):
            return move
    
def emptyBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                return False
    return True

def AIchoice(boards, player2):
    import numpy as np
    if len(boards) == 3:
        if sacrifice(board_a):
            return "A" + sacrifice(board_a)
        elif sacrifice(board_b):
            return "B" + sacrifice(board_b)
        elif sacrifice(board_c):
            return "C" + sacrifice(board_c)
        elif emptyBoard(board_b):
            return "B4"
        elif emptyBoard(board_c):
            return "C4"
        elif trap_2X(board_b):
            return "B" + trap_2X(board_b)
        elif trap_2X(board_c):
            return "C" + trap_2X(board_c)
    elif len(boards) == 2:
        if emptyBoard(board_b):
            return "B4"
        elif emptyBoard(board_c):
            return "C4"
        if player2[0] == "A" and board_a[1][1] == "X" and ((board_b in boards and board_b[1][1] == "X") or (board_c in boards and board_c[1][1] == "X")):
            return "A" + sacrifice(board_a)
        elif player2[0] == "B" and board_b[1][1] == "X" and ((board_a in boards and board_a[1][1] == "X") or (board_c in boards and board_c[1][1] == "X")):
            return "B" + sacrifice(board_b)
        elif player2[0] == "C" and board_c[1][1] == "X"  and ((board_b in boards and board_b[1][1] == "X") or (board_a in boards and board_a[1][1] == "X")):
            return "C" + sacrifice(board_c)
        else:
            if player2[0] == "A":
                if trap_2X(board_a) and np.in1d(board_a,"X").sum() == 2:
                    return "A" + trap_2X(board_a)
                elif (board_c[1][1] != "X" or board_b[1][1] != "X"):
                    return "A" + str(knightsMove(board_a,int(player2[1])))
                elif board_a[1][1] == "X" or (board_b[1][1] == "X" or board_c[1][1] == "X"):
                    return "A" + sacrifice(board_a)
            elif player2[0] == "B":
                if trap_2X(board_b) and np.in1d(board_b,"X").sum() == 2:
                    return "B" + trap_2X(board_b)
                elif (board_a[1][1] != "X" or board_c[1][1] != "X"):
                    return "B" + str(knightsMove(board_b,int(player2[1])))
                elif (board_b[1][1] == "X" or (board_a[1][1] == "X" or board_c[1][1] == "X")):
                    return "B" + sacrifice(board_b)
            elif player2[0] == "C":
                if trap_2X(board_c) and np.in1d(board_c,"X").sum() == 2:
                    return "C" + trap_2X(board_c)
                elif (board_a[1][1] != "X" or board_b[1][1] != "X"):
                    return "C" + str(knightsMove(board_c,int(player2[1])))
                elif board_c[1][1] == "X" or (board_b[1][1] == "X"or board_a[1][1] == "X"):
                    return "C" + sacrifice(board_c)
    else:
        for i in boards:
            if player2[1] != i[1][1]:
                if i[1][1] == "X":
                    return alphabets[0] + str(knightsMove(i,int(player2[1])))
                elif mirrorMove(i):
                    return alphabets[0] + mirrorMove(i)
                elif trap_2X(i) and np.in1d(i,"X").sum() == 2:
                    return alphabets[0] + trap_2X(i)
                else:
                    return alphabets[0] + str(knightsMove(i,int(player2[1])))

def main(boards):
    taken = []
    print_board()
    print("Player 1: A4")
    insertBoard(board_a,"4")
    while True:
        if len(boards) == 0:
            print("Player 2 wins game")
            return
        print_board()
        player2 = input("Player 2: ")
        while (player2[1:] not in digits) or (len(player2) != 2) or (player2[0] not in alphabets) or (player2 in taken):
            print("Invalid move, please input again")
            player2 = input("Player 2: ")
        if player2[0] in alphabets:
            taken.append(player2)
            if player2[0] == "A":
                insertBoard(board_a,player2[1])
                removingBoard("A",board_a)
            elif player2[0] == "B":
                insertBoard(board_b,player2[1])
                removingBoard("B",board_b)
            else:
                insertBoard(board_c,player2[1])
                removingBoard("C",board_c)
        if len(boards) == 0:
            print("Player 1 wins game")
            return
        print_board()
        player1 = AIchoice(boards,player2)
        print("Player 1:",player1)
        if player1[0] in alphabets:
            if player1[0] == "A":
                insertBoard(board_a,player1[1])
                removingBoard("A",board_a)
            elif player1[0] == "B":
                insertBoard(board_b,player1[1])
                removingBoard("B",board_b)
            else:
                insertBoard(board_c,player1[1])
                removingBoard("C",board_c)
                
main(boards)