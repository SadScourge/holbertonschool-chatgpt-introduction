def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("---+---+---")  # Adjusted to match the board layout

def check_winner(board):
	# Check rows for a win
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return row[0]  # Return the winning player

	# Check columns for a win
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return board[0][col]  # Return the winning player

	# Check diagonals for a win
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return board[0][0]  # Return the winning player

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return board[0][2]  # Return the winning player

	return None  # No winner yet

def is_board_full(board):
	# Check if all cells are filled
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "] * 3 for _ in range(3)]
	player = "X"
	while True:
		print_board(board)
		# Input validation loop
		while True:
			try:
				row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
				col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
				if row not in [0, 1, 2] or col not in [0, 1, 2]:
					print("Please enter values between 0 and 2.")
				elif board[row][col] != " ":
					print("That spot is already taken! Try again.")
				else:
					break  # Valid input
			except ValueError:
				print("Invalid input. Please enter numeric values.")

		# Place the player's mark on the board
		board[row][col] = player
		# Check for a winner
		winner = check_winner(board)
		if winner:
			print_board(board)
			print(f"Player {winner} wins!")
			break

		# Check for a tie
		if is_board_full(board):
			print_board(board)
			print("It's a tie!")
			break

		# Switch players
		player = "O" if player == "X" else "X"

if __name__ == "__main__":
	tic_tac_toe()
