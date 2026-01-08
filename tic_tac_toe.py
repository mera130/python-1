theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'x'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("its your turn" , turn , "move")
        move = input()
        if theBoard[move]== " ":
            theBoard[move] = turn
            count+=1
        else:
            print('that place is already taken \n')
            continue
        if count >= 5:
            if theBoard['7']==['8']==['9']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + '***WONN****')
                break
            elif  theBoard['4']==['5']==['6']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['1']==['2']==['3']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['1']==['4']==['7']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['2']==['5']==['8']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['3']==['6']==['9']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['7']==['5']==['3']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
            elif  theBoard['1']==['5']==['9']!=' ':
                print('\n GAME OVER!! \n')
                print('****' + turn + 'WONN****')
                break
                
        if count == 9:
            print('\n GAME OVER \n')
            print('its a tie!!')
            
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'o'
    restart = input('wanna play again(y/n): ')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key]=' '
        game()
if __name__ == '__main__':
    game()