import sys
from copy import deepcopy

class Minimax:
	def __init__(self):
		self.empty = ' '
		self.computer_sign = 'O'
		self.player_sign = 'X'
		self.game_size = 3

	def algorithm(self, board):
		utility = -sys.maxint - 1
		pos = {}
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
		for x in range(self.game_size):
			for y in range(self.game_size):
				if board[x][y] == self.empty:
					return False
		return True

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
