import sys
from copy import deepcopy

class Minimax:
	def __init__(self, game):
		self.empty = ' '
		self.computer_sign = 'O'
		self.player_sign = 'X'
		if game == "connect4":
			self.row_size = 7
			self.column_size = 9
		else:	
			self.game_size = 3
		self.game = game # either connect4 or tictactoe

	def algorithm(self, board):
		utility = -sys.maxint - 1
		pos = {}
		if self.game == "connect4":
			for i in range(self.row_size):
				j = board[i].count('X') + board[i].count('O')
				if j < self.column_size:
					newboard = deepcopy(board)
					newboard[i][j] = self.computer_sign
					temp_utility = self.connect4_min_comp(newboard, 0)
					if (temp_utility > utility):
						utility = temp_utility
						pos = (i, j)
		else:
			for i in range(self.game_size):
				for j in range(self.game_size):
					if board[i][j] == self.empty:
						newboard = deepcopy(board)
						newboard[i][j] = self.computer_sign
						temp_utility = self.min_comp(newboard)
						if (temp_utility > utility):
							utility = temp_utility
							pos = (i, j)
		return pos;

	def connect4_min_comp(self, board, depth):
		board_val = self.connect4_check_val(board)
		depth += 1
		if (board_val != 0 or depth > 5 or self.all_filled(board)): # depth no greater than 5? this is arbitrary, so we can change
			return board_val
		utility = sys.maxint
		for i in range(self.row_size):
			j = board[i].count('X') + board[i].count('O')
			if j < self.column_size:
				newboard = deepcopy(board)
				newboard[i][j] = self.player_sign
				temp_utility = self.connect4_max_comp(newboard, depth)
				if (temp_utility > utility):
					utility = temp_utility
		return utility
		

	def connect4_max_comp(self, board, depth):
		board_val = self.connect4_check_val(board)
		depth += 1
		if (board_val != 0 or depth > 5 or self.all_filled(board)): # depth no greater than 5? this is arbitrary, so we can change
			return board_val
		utility = -sys.maxint - 1
		for i in range(self.row_size):
			j = board[i].count('X') + board[i].count('O')
			if j < self.column_size:
				newboard = deepcopy(board)
				newboard[i][j] = self.computer_sign
				temp_utility = self.connect4_min_comp(newboard, depth)
				if (temp_utility > utility):
					utility = temp_utility
		return utility

	def min_comp(self, board):
		board_val = self.check_val(board)
		if (board_val != 0 or self.all_filled(board)):
			return board_val
		utility = sys.maxint
		for i in range(self.game_size):
			for j in range(self.game_size):
				if board[i][j] == self.empty:
					newboard = deepcopy(board)
					newboard[i][j] = self.player_sign
					temp_utility = self.max_comp(newboard)
					if (temp_utility < utility):
						utility = temp_utility
		return utility;

	def max_comp(self, board):
		board_val = self.check_val(board)
		if (board_val != 0 or self.all_filled(board)):
			return board_val
		utility = -sys.maxint - 1
		for i in range(self.game_size):
			for j in range(self.game_size):
				if board[i][j] == self.empty:
					newboard = deepcopy(board)
					newboard[i][j] = self.computer_sign
					temp_utility = self.min_comp(newboard)
					if (temp_utility > utility):
						utility = temp_utility
		return utility;

	def all_filled(self, board):
		if self.game == "connect4":
			for x in range(self.row_size):
				for y in range(self.column_size):
					if board[x][y] == self.empty:
						return False
		else:
			for x in range(self.game_size):
				for y in range(self.game_size):
					if board[x][y] == self.empty:
						return False
		return True

	def connect4_check_val(self, board):
		# if any rows of 4 pieces are completed
		for x in range(self.row_size):
			for y in range(self.column_size-4):
				player_spot = board[x][y]
				if player_spot != self.empty:
					for y_move in range(y, y+3):
						if player_spot != board[x][y_move]:
							if y_move == y+2:  #only 2 in a row (3rd spot not there)
								if (player_spot == self.player_sign):
									return -0.5
								elif (player_spot == self.computer_sign):
									return 0.5
							elif y_move == y+3: #only 3 in a row (4th spot not there)
								if (player_spot == self.player_sign):
									return -0.75
								elif (player_spot == self.computer_sign):
									return 0.75
							break
						elif y_move == y+3:
							if (player_spot == self.player_sign):
								return -1
							elif (player_spot == self.computer_sign):
								return 1

		# check if any columns w/ 4 pieces are completed
		for y in range(self.column_size):
			for x in range(self.row_size-4):
				player_spot = board[x][y]
				if player_spot != self.empty:
					for x_move in range(x, x+3):
						if player_spot != board[x_move][y]:
							if x_move == x+2: #only 2 in a row (3rd spot not there)
								if (player_spot == self.player_sign):
									return -0.5
								elif (player_spot == self.computer_sign):
									return 0.5
							elif x_move == x+3: #only 3 in a row (4th spot not there)
								if (player_spot == self.player_sign):
									return -0.75
								elif (player_spot == self.computer_sign):
									return 0.75
							break
						elif x_move == x+3:
							if (player_spot == self.player_sign):
								return -1
							elif (player_spot == self.computer_sign):
								return 1

		for i in range(self.row_size - 1, -1, -1):
			mark = board[i][0]
			num = 0
			for j in range(self.column_size + self.row_size):
				new_col = i + j
				if new_col >= self.row_size:
					break
				if j >= self.column_size:
					break
				if board[new_col][j] == mark and board[new_col][j] != self.empty:
					num += 1
					if num == 4:
						if mark == self.player_sign:
							return -1
						elif (mark == self.computer_sign):
							return 1
				else:
					if num == 2:
						if mark == self.player_sign:
							return -0.5
						elif (mark == self.computer_sign):
							return 0.5
					elif num == 3:
						if mark == self.player_sign:
							return -0.75
						elif (mark == self.computer_sign):
							return 0.75
					num = 0
					mark = board[new_col][j]

		for i in range(self.row_size):
			mark = board[0][i]
			num = 0
			for j in range(i, self.column_size + self.row_size):
				new_col = j - i 
				if new_col >= self.row_size:
					break
				if j >= self.column_size:
					break
				if board[new_col][j] == mark and board[new_col][j] != self.empty:
					num += 1
					if num == 4:
						if mark == self.player_sign:
							return -1
						elif (mark == self.computer_sign):
							return 1
				else:
					if num == 2:
						if mark == self.player_sign:
							return -0.5
						elif (mark == self.computer_sign):
							return 0.5
					elif num == 3:
						if mark == self.player_sign:
							return -0.75
						elif (mark == self.computer_sign):
							return 0.75
					num = 0
					mark = board[new_col][j]

		for i in range(self.row_size):
			mark = board[i][0]
			num = 0
			for j in range(self.row_size + self.column_size):
				new_col = i - j
				if new_col >= self.row_size or new_col < 0:
					break
				if j >= self.column_size:
					break
				if board[new_col][j] == mark and board[new_col][j] != self.empty:
					num += 1
					if num == 4:
						if mark == self.player_sign:
							return -1
						elif (mark == self.computer_sign):
							return 1
				else:
					if num == 2:
						if mark == self.player_sign:
							return -0.5
						elif (mark == self.computer_sign):
							return 0.5
					elif num == 3:
						if mark == self.player_sign:
							return -0.75
						elif (mark == self.computer_sign):
							return 0.75
					num = 0
					mark = board[new_col][j]

		for i in range(self.column_size):
			mark = board[self.row_size - 1][0]
			num = 0
			for j in range(self.row_size + self.column_size):
				new_col = self.row_size - 1 - j
				if new_col >= self.row_size or new_col < 0:
					break
				if j >= self.column_size:
					break
				if board[new_col][j] == mark and board[new_col][j] != self.empty:
					num += 1
					if num == 4:
						if mark == self.player_sign:
							return -1
						elif (mark == self.computer_sign):
							return 1
				else:
					if num == 2:
						if mark == self.player_sign:
							return -0.5
						elif (mark == self.computer_sign):
							return 0.5
					elif num == 3:
						if mark == self.player_sign:
							return -0.75
						elif (mark == self.computer_sign):
							return 0.75
					num = 0
					mark = board[new_col][j]


		# TODO: check diagonals

		return 0


	def check_val(self, board):
		# check if any rows are completed
		for x in range(self.game_size):
			player_spot = board[x][0]
			if player_spot != self.empty:
				for y in range(1, self.game_size):
					if player_spot != board[x][y]:
						break
					elif y == self.game_size - 1: # todo diff function
						if (player_spot == self.player_sign):
							return -1
						elif (player_spot == self.computer_sign):
							return 1
		# check if any columns are completed
		for y in range(self.game_size):
			player_spot = board[0][y]
			if player_spot != self.empty:
				for x in range(1, self.game_size):
					if player_spot != board[x][y]:
						break
					elif x == self.game_size - 1:
						if (player_spot == self.player_sign):
							return -1
						elif (player_spot == self.computer_sign):
							return 1

		# check diagonal top left to bottom right (0,0) (1,1) (2,2)
		player_spot = board[0][0]
		if player_spot != self.empty:
			for x in range(1, self.game_size):
				if player_spot != board[x][x]:
					break
				elif x == self.game_size - 1:
					if (player_spot == self.player_sign):
						return -1
					elif (player_spot == self.computer_sign):
						return 1

		# check diagonal top right to bottom left (2,0) (1,1) (0,2)
		player_spot = board[2][0]
		if player_spot != self.empty:
			for x in range(1, self.game_size):
				if player_spot != board[2-x][x]:
					break
				elif x == self.game_size - 1:
					if (player_spot == self.player_sign):
						return -1
					elif (player_spot == self.computer_sign):
						return 1

		return 0
