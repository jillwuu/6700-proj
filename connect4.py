import random
from minimax import Minimax 

class Connect4:
	def __init__(self):
		# 6 rows, 7 columns
		self.minimax = Minimax("connect4")
		self.row_size = 7 #number of columns
		self.column_size = 9 #number of rows
		self.player_0 = 'X'
		self.player_1 = 'O'
		self.player = self.player_0
		self.empty = ' '
		self.board = [[self.empty for _ in range(self.column_size)] for _ in range(self.row_size)]
		self.game_over = False
		self.winner = None

		self.empty_spots = []
		for i in range(self.row_size):
			for j in range(self.column_size):
				self.empty_spots.append((i, j))

	def display_board(self):
		row_divide = "--" + ("----" * (self.row_size - 1)) + "---"
		for x in range(self.column_size):
			curr_row = ""
			for y in range(self.row_size):
				if y < self.column_size - 1:
					curr_row = curr_row + self.board[y][self.column_size - x - 1] + " | "
				else:
					curr_row = curr_row + self.board[y][self.column_size - x - 1]
			print(curr_row)
			if x != self.column_size-1:
				print(row_divide)

	def update_board(self, player, column):
		if column < self.row_size:
			curr_filled = self.board[column].count('X') + self.board[column].count('O')
			if curr_filled < self.column_size:
				self.board[column][curr_filled] = player
			else:
				print("This column is already filled, please enter another location")
		else:
			print("invalid location, please enter another location")
		# self.empty_spots.remove(location)
		self.display_board()
		if self.player == self.player_0:
			self.player = self.player_1
		else:
			self.player = self.player_0

		# self.check_win()
		# if not self.game_over:
		# 	print("IT IS NOW PLAYER " + self.player + "'S TURN")

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
		for y in range(self.column_size):
			if self.game_over == False:
				player_spot = self.board[0][y]
				if player_spot != self.empty:
					for x in range(1, self.row_size):
						if player_spot != self.board[x][y]:
							break
						elif x == self.row_size - 1:
							self.winner = player_spot
							self.game_over = True

		# check diagonal top left to bottom right (0,0) (1,1) (2,2)
		if self.game_over == False:
			player_spot = self.board[0][0]
			if player_spot != self.empty:
				for x in range(1, self.row_size):
					if player_spot != self.board[x][x]:
						break
					elif x == self.row_size - 1:
						self.winner = player_spot
						self.game_over = True

		# check diagonal top right to bottom left (2,0) (1,1) (0,2)
		if self.game_over == False:
			player_spot = self.board[2][0]
			if player_spot != self.empty:
				for x in range(1, self.row_size):
					if player_spot != self.board[2-x][x]:
						break
					elif x == self.row_size - 1:
						self.winner = player_spot
						self.game_over = True

		self.game_over = self.minimax.all_filled(self.board)

	# def computer_move(self):
	# 	computer_loc = (self.minimax.algorithm(self.board))
		# self.update_board(self.player, computer_loc)


	def player_move(self):
		x = input("Please choose a column to place your piece: ")
		self.update_board(self.player, int(x))
		

	def play(self):
		print(self.board)
		print(self.display_board())
		print("IT IS NOW PLAYER " + self.player + "'S TURN")
		while not self.game_over:
			self.player_move()
			# if not self.game_over:
			# 	self.computer_move()
		if self.winner:
			print("GAME OVER, " + self.winner + " HAS WON")
		else:
			print("GAME OVER, TIE!")


game = Connect4()
game.play()
