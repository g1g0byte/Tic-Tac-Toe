import os

def game_handling():
	player_scores = {'X': 0, 'O': 0, 'Draw' : 0}
	current_player = 'O'
	while True:
		clear_console()

		# Switch current player after every game
		current_player = switch_player(current_player)

		# Play a single game
		winning_player = single_game(current_player)

		# Update the scores
		player_scores[winning_player] += 1

		# Print the scores
		print("----------")
		print("X - " + str(player_scores['X']))
		print("O - " + str(player_scores['O']))
		print("Draws - " + str(player_scores['Draw']))
		print("----------\n")

		# Get if user wants to play again
		play_again = play_again_input()
		
		# Check if the input is "yes" or "no"
		if play_again in ['y','Y']:
			continue
		else:
			break

def single_game(current_player):
	# Set default values for new game
	cell_values = [' ' for i in range(9)]
	player_positions = {'X':[], 'O':[]}

	print_tic_tac_toe(cell_values)
	while True:
		clear_console()

		# Print the game grid with updated cells
		print_tic_tac_toe(cell_values)

		# Get current players input
		selected_cell = player_cell_input(current_player, cell_values)

		# Update the value of the cell chosen
		cell_values[selected_cell-1] = current_player
		
		# Add chosen cell to current players positions list
		player_positions[current_player].append(selected_cell)

		# Check if the current player has won by comparing to winning combinations
		if check_win(player_positions, current_player) == True:
			clear_console()
			print_tic_tac_toe(cell_values)
			print("Player " + current_player + " has won!\n")
			#Return to game handling loop and pass through the winning player
			return current_player

		# Check if the game is drawn by checking if 9 moves have been played
		if len(player_positions['X']) + len(player_positions['O']) == 9:
			clear_console()
			print_tic_tac_toe(cell_values)
			print("Game is a draw\n")
			#Set current player to 'Draw' so we know neither player won
			current_player = 'Draw'
			return current_player

		print(current_player)
		# Switch current player
		current_player = switch_player(current_player)

def check_win(player_positions, current_player):
	# Array of all possible winning cell combinations
	winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

	# Loop to check if any winning combination is satisfied
	for x in winning_combinations:
		if all(y in player_positions[current_player] for y in x):
			# Return True if any winning combination satisfies
			return True
	# Return False if no combination is satisfied		
	return False		

def print_tic_tac_toe(cell_values):
	print("\n")
	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(cell_values[0], cell_values[1], cell_values[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(cell_values[3], cell_values[4], cell_values[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(cell_values[6], cell_values[7], cell_values[8]))
	print("\t     |     |")
	print("\n")

def player_cell_input(current_player, cell_values):
	while True:
		try:
			selected_cell = int(input("Player " + current_player + "'s turn. Enter which cell: "))
		# Handle if input is not an integer
		except ValueError:
			print("Please enter an integer cell number!\n")
		else:
			# Check if selected_cell is  between 1-9
			if selected_cell < 1 or selected_cell > 9:
				print("Enter a cell number between 1-9!\n")
				continue
			# Check if the cell has already been chosen
			if cell_values[selected_cell-1] != ' ':
				print("That cell is already chosen!\n")
			else:
				return selected_cell

def play_again_input():
	while True:
		try:
			play_again = input("Would you like to play again? (y/n) : ")
		# Handle if input is not an integer
		except TypeError:
			print("Please enter a letter (y/n)!\n")
		else:
			# Check if input is a valid answer
			if play_again not in ['y','Y','n','N']:
				print("Please enter 'y' or 'n'!\n")
				continue
			else:
				return play_again

def switch_player(current_player):
	if current_player == 'X':
		current_player = 'O'
	else:
		current_player = 'X'
	return current_player

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

# Main Program
game_handling()