import random

n = int(input("Please enter your n x n dimension: "))
chess_char = int(input("Please enter your checking character: "))

chess_board = [[random.randint(0,10) for _ in range(n)] for _ in range(n)]

length_list = len(chess_board)

def Knights_move(chess_board,chess_char):
    
    cnt=0

    for row in range(length_list):

        for col in range(length_list):

            for row1,col1 in [(row+1,col+2),(row+1,col-2),(row+2, col+1),(row+2,col-1),(row-1,col+2),(row-1,col-2),(row-2, col+1),(row-2,col-1)]:

                if (0 <= row1 < length_list) and (0 <= col1 < length_list):

                    if (chess_board[row][col] * chess_board[row1][col1] == chess_char):

                        cnt+=1

    print (chess_board)
    print ("Number of pair elements: " + str(cnt//2))

Knights_move(chess_board, chess_char)