theBoard = {'a': ' ' , 'b': ' ' , 'c': ' ' ,
            'd': ' ' , 'e': ' ' , 'f': ' ' ,
            'g': ' ' , 'h': ' ' , 'i': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['a'] + '|' + board['b'] + '|' + board['c'])
    print('-+-+-')
    print(board['d'] + '|' + board['e'] + '|' + board['f'])
    print('-+-+-')
    print(board['g'] + '|' + board['h'] + '|' + board['i'])


def game():

    turn = 'karthi'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

       
        if count >= 5:
            if theBoard['a'] == theBoard['b'] == theBoard['c'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['d'] == theBoard['e'] == theBoard['f'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['g'] == theBoard['h'] == theBoard['i'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['g'] == theBoard['d'] == theBoard['a'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['h'] == theBoard['e'] == theBoard['b'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['c'] == theBoard['6'] == theBoard['c'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['a'] == theBoard['e'] == theBoard['i'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['g'] == theBoard['e'] == theBoard['c'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='karthi':
            turn = 'seenu'
        else:
            turn = 'karthi'        
    

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()