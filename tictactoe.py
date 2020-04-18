class TicTacToe:
	def __init__(self):
		self.game_size = 3
		self.player_0 = 'X'
		self.player_1 = 'O'
		self.player = self.player_0
		self.empty = ' '
		self.board = [[self.empty for _ in range(self.game_size)] for _ in range(self.game_size)]
		self.game_over = False
		self.winner = None

	def display_board(self):
		row_divide = "---------"
		for x in range(self.game_size):
			curr_row = ""
			for y in range(self.game_size):
				if y == 0 or y == 1:
					curr_row = curr_row + self.board[x][y] + " | "
				else:
					curr_row = curr_row + self.board[x][y]
			print(curr_row)
			if x == 0 or x == 1:
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
		# check if any rows are completed
		for x in range(self.game_size):
			if self.game_over == False:
				player_spot = self.board[x][0]
				if player_spot != self.empty:
					for y in range(1, self.game_size):
						if player_spot != self.board[x][y]:
							break
						elif y == self.game_size - 1:
							self.winner = player_spot
							self.game_over = True

		# check if any columns are completed
		for y in range(self.game_size):
			if self.game_over == False:
				player_spot = self.board[0][y]
				if player_spot != self.empty:
					for x in range(1, self.game_size):
						if player_spot != self.board[x][y]:
							break
						elif x == self.game_size - 1:
							self.winner = player_spot
							self.game_over = True

		# check diagonal top left to bottom right (0,0) (1,1) (2,2)
		if self.game_over == False:
			player_spot = self.board[0][0]
			if player_spot != self.empty:
				for x in range(1, self.game_size):
					if player_spot != self.board[x][x]:
						break
					elif x == self.game_size - 1:
						self.winner = player_spot
						self.game_over = True

		# check diagonal top right to bottom left (2,0) (1,1) (0,2)
		if self.game_over == False:
			player_spot = self.board[2][0]
			if player_spot != self.empty:
				for x in range(1, self.game_size):
					if player_spot != self.board[2-x][x]:
						break
					elif x == self.game_size - 1:
						self.winner = player_spot
						self.game_over = True




	def player_move(self):
		x = input("Please choose an x coordinate: ")
		y = input("Please choose a y coordinate: ")
		self.update_board(self.player, (int(x), int(y)))
		if self.player == self.player_0:
			self.player = self.player_1
		else:
			self.player = self.player_0

	def play(self):
		while not self.game_over:
			self.player_move()
			self.display_board()
			self.check_win()

		print("GAME OVER, " + self.winner + " HAS WON")


game = TicTacToe()
game.play()