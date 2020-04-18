class TicTacToe:
	def __init__(self):
		self.game_size = 3
		self.player_0 = 'X'
		self.player_1 = 'O'
		self.player = self.player_0
		self.empty = ' '
		self.board = [[self.empty for _ in range(self.game_size)] for _ in range(self.game_size)]
		self.game_over = False

	def display_board(self):
		row_divide = "---------"
		for y in range(self.game_size):
			curr_row = ""
			for x in range(self.game_size):
				if x == 0 or x == 1:
					curr_row = curr_row + self.board[x][y] + " | "
				else:
					curr_row = curr_row + self.board[x][y]
			print(curr_row)
			if y == 0 or y == 1:
				print(row_divide)

	def update_board(self, player, location):
		(x, y) = location
		if x < 3 and y < 3:
			if self.board[x][y] == self.empty:
				self.board[x][y] = player
			else:
				print("This location is already filled, please enter another location")
		else:
			print("invalid location, please enter another location")

	def check_win(self):
		pass

	def player_move(self):
		x = input("Please choose an x coordinate: ")
		y = input("Please choose a y coordinate: ")
		self.update_board(self.player, (int(x), int(y)))

	def play(self):
		print("testing")
		# self.update_board(self.player_0, (0, 1))
		# self.update_board(self.player_0, (0, 1))
		self.player_move()
		print(self.board)
		self.display_board()


game = TicTacToe()
game.play()