#Create dictionary for players move
#Create array storing cell information ('empty', 'X, or 'O')-----

#Create array for storing players scores--------
#Create array for storing all possible winning cell combinations (e.g. 1,2,3)

#Function to switch players ('X' to 'O')
#Function to get user input and validate it
#Function to check if a player has won after their turn
#Function to check if game is drawn
#Function to get current players input
#Print score on scoreboard
cell_values = [' ' for x in range(9)]
player_positions = {'X':[], 'O':[]}
player_scores = [0,0]
solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def single_game():
	current_player = 'X'
	#Print the game grid
	print_tic_tac_toe(cell_values)

	#Get current players input
	player_input(current_player)
	print("outa ehre")

def print_tic_tac_toe(cell_values):
	print("\n")
	print("\t     |     |")
	print("\t   {} |  {}  |  {}".format(cell_values[0], cell_values[1], cell_values[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t   {} |  {}  |  {}".format(cell_values[3], cell_values[4], cell_values[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t   {} |  {}  |  {}".format(cell_values[6], cell_values[7], cell_values[8]))
	print("\t     |     |")
	print("\n")

def player_input(current_player):
	while True:
		try:
			selected_cell = int(input("Player " + current_player + "'s turn. Enter which cell: "))
			break
		except:
			print("Invalid Input! Please enter a cell number\n")


#Main Program
single_game()