global board

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
player = "X"
''' Print board'''
def printBoard(board):
    for line in board:
        print(line)
        
        
''' Make a move from user'''        
def makeMove():
    global player
    x = int(input("Player "+player +" ,What is the X coordinate? "))
    y = int(input("What is the Y coordinate? "))
    
    while board[y][x] != " ":
        print("You must choose an empty spot")
        x = int(input("Player "+player +" ,What is the X coordinate? "))
        y = int(input("What is the Y coordinate? "))
    
    if player == "X":
        board[y][x] = "X"
        player = "O"
    else:
        board[y][x] = "O"
        player = "X"

'''win'''
def isWin():
	global player
	if player == "X":
		p = "O"
	else:
		p = "X"
	#row
	for c in range(len(board)):
		win = True
		for r in range(len(board)):
			if board[c][r] != p:
				win = False
				break
		if win:
			return True
	#column
	for c in range(len(board)):
		win = True
		for r in range(len(board)):
			if board[r][c] != p:
				win = False
				break
		if win:
			return True
	#diagonals
	win = True
	for c in range(3):
		if board[c][c] != p:
			win = False
			break
	if win:
		return True

	win = True
	for r in range(len(board)):
		if board[r][len(board)-1-r] != p:
			win = False
			break
	if win:
		return True


	return False
    

    


    
def main():
	gamewon = False
	while gamewon == False:
		printBoard(board)
		makeMove()
		gamewon = isWin()
	print("PLAYER "+player+ " WON!")
	printBoard(board)
    
    
    

main()