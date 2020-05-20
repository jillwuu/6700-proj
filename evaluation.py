from connect4 import Connect4

text_file = open("Output4.txt", "w")

text_file.write("4 goes first")

i_win = 0
j_win = 0
tie = 0
for n in range(30):
	game = Connect4(3, 4, 3, 2)
	result = game.evaluate()
	if result == "X":
		i_win += 1
	elif result == "O":
		j_win += 1
	else:
		tie += 1

text_file.write("Heuristic 4: %d,\nHeuristic 2: %d, \nTie: %d\n" % (i_win, j_win, tie))

text_file.write("2 goes first")

i_win = 0
j_win = 0
tie = 0
for n in range(30):
	game = Connect4(3, 2, 3, 4)
	result = game.evaluate()
	if result == "X":
		i_win += 1
	elif result == "O":
		j_win += 1
	else:
		tie += 1

text_file.write("Heuristic 2: %d,\nHeuristic 4: %d, \nTie: %d\n" % (i_win, j_win, tie))


text_file.close()
