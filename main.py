import random
import keyboard
import time


#def init_Score():
	#global score
	#score = 0

def make_Grid(size):  #Makes 4 by 4 grid
	global grid
	grid = [[0 for i in range(size)] for j in range(size)]  #0 for empty spaces



#############


def check_Grid():
	"""Checks if grid is full, and locates and returns a list of empty spaces in grid to insert values into"""
	global emptySpaces
	emptySpaces = []
	playCanBeMade = False


	for i in range(4):
		for j in range(4):
			if grid[i][j] == 0:
				emptySpaces.append((i, j))

			elif grid[i][j] == 2048:
				print("Congratulations You Won The Game!")
				#print(f"Final #score: {#score}")
				quit()  #Implement way to start new game later or something

			elif i == 0:
				if grid[i][j] == grid[i+1][j]:
					playCanBeMade = True

				if j < 3:
					if grid[i][j] == grid[i][j+1]:
						playCanBeMade = True
				
			elif i == 1:
				if grid[i][j] == grid[i+1][j]:
					playCanBeMade = True

				if j < 3:
					if grid[i][j] == grid[i][j+1]:
						playCanBeMade = True
				
			elif i == 2:
				if grid[i][j] == grid[i+1][j]:
					playCanBeMade = True

				if j < 3:
					if grid[i][j] == grid[i][j+1]:
						playCanBeMade = True
				
	#print(emptySpaces)

	if emptySpaces == [] and playCanBeMade == False:
		print("No empty spaces left!")
		#print(f"Final #score: {score}")
		print("Gameover!")
		quit()  #Implement way to start new game later or something
	else:
		#print(emptySpaces)
		pass


#############


def shift():
	"""Shifts numbers on the grid into the direction the user decides, returns a value "last shift" which shows which direction was last used"""
	direction = ""
	while direction not in ("up", "down", "left", "right"):
		direction = keyboard.read_key();"""UPDATE MAKE NICER TO USE LATER"""

	#shiftMade = False

	#UP
	if keyboard.is_pressed("up"):  #Start up to down
		for i in range(4):  #check top down, closest first go up
			if i == 0:
				continue

			else:
				for j in range(4):  #left to right
					if grid[i][j] != 0:

						if i == 1:

							if grid[i - 1][j] == 0:
								grid[i - 1][j] = grid[i][j]
								grid[i][j] = 0
								combine(direction)

						elif i == 2:

							if grid[i - 1][j] == 0:
								if grid[i - 2][j] == 0:
									grid[i - 2][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

								else:
									grid[i - 1][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

						elif i == 3:

							if grid[i - 1][j] == 0:
								if grid[i - 2][j] == 0:
									if grid[i - 3][j] == 0:
										grid[i - 3][j] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

									else:
										grid[i - 2][j] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

								else:
									grid[i - 1][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)
					else:
						pass

		return "up"

	#DOWN
	elif keyboard.is_pressed("down"):  #start up down

		for i in range(3, -1, -1):  #check down to up, closest first go down
			if i == 3:
				continue

			else:
				for j in range(4):  #left to right
					if grid[i][j] != 0:

						if i == 2:

							if grid[i + 1][j] == 0:
								grid[i + 1][j] = grid[i][j]
								grid[i][j] = 0
								combine(direction)

						elif i == 1:

							if grid[i + 1][j] == 0:
								if grid[i + 2][j] == 0:
									grid[i + 2][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

								else:
									grid[i + 1][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

						elif i == 0:

							if grid[i + 1][j] == 0:
								if grid[i + 2][j] == 0:
									if grid[i + 3][j] == 0:
										grid[i + 3][j] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

									else:
										grid[i + 2][j] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

								else:
									grid[i + 1][j] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

					else:
						pass

		return "down"

	#LEFT
	elif keyboard.is_pressed("left"):  #start right to left
		for j in range(4):  #check left to right, closest first go left
			if j == 0:
				continue

			else:
				for i in range(4):  #left to right
					if grid[i][j] != 0:
						#has a number inside

						if j == 1:

							if grid[i][j - 1] == 0:
								grid[i][j - 1] = grid[i][j]
								grid[i][j] = 0
								combine(direction)

						elif j == 2:

							if grid[i][j - 1] == 0:
								if grid[i][j - 2] == 0:
									grid[i][j - 2] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

								else:
									grid[i][j - 1] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

						elif j == 3:

							if grid[i][j - 1] == 0:
								if grid[i][j - 2] == 0:
									if grid[i][j - 3] == 0:
										grid[i][j - 3] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

									else:
										grid[i][j - 2] = grid[i][j]
										grid[i][j] = 0
										combine(direction)
								else:
									grid[i][j - 1] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

					else:
						pass

		return "left"

	#RIGHT
	elif keyboard.is_pressed("right"):  #start left to right
		for j in range(3, -1, -1):  #check right to left, closest first goes right
			if j == 3:
				continue

			else:
				for i in range(4):  #left to right
					if grid[i][j] != 0:
						#has a number inside

						if j == 2:

							if grid[i][j + 1] == 0:
								grid[i][j + 1] = grid[i][j]
								grid[i][j] = 0
								combine(direction)

						elif j == 1:

							if grid[i][j + 1] == 0:
								if grid[i][j + 2] == 0:
									grid[i][j + 2] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

								else:
									grid[i][j + 1] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

						elif j == 0:

							if grid[i][j + 1] == 0:
								if grid[i][j + 2] == 0:
									if grid[i][j + 3] == 0:
										grid[i][j + 3] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

									else:
										grid[i][j + 2] = grid[i][j]
										grid[i][j] = 0
										combine(direction)

								else:
									grid[i][j + 1] = grid[i][j]
									grid[i][j] = 0
									combine(direction)

					else:
						pass

		return "right"


#############


def combine(direction):
	"""If two matching numbers are shifted into each other they are to be combined(added together"""
	if direction == "up":
		for i in range(3):  #Indexes from 0 to 2 as check is for the next number down, so when i == 2, it will already check for grid[i+1][j]
			for j in range(4):  #indexs normally left to right as only chekcign down on this one
				if grid[i + 1][j] == grid[i][j]:
					grid[i][j] = grid[i][j] * 2
					grid[i + 1][j] = 0
					#score += grid[i][j]

	elif direction == "down":

		for i in range(3, 0, -1):
			for j in range(4):
				if grid[i - 1][j] == grid[i][j]:
					grid[i][j] = grid[i][j] * 2
					grid[i - 1][j] = 0
					#score += grid[i][j]

	elif direction == "left":

		for j in range(3):
			for i in range(4):
				if grid[i][j + 1] == grid[i][j]:
					grid[i][j] = grid[i][j] * 2
					grid[i][j + 1] = 0
					#score += grid[i][j]

	elif direction == "right":
		for j in range(3, 0, -1):
			for i in range(4):
				if grid[i][j - 1] == grid[i][j]:
					grid[i][j] = grid[i][j] * 2
					grid[i][j - 1] = 0
				#	score += grid[i][j]


#############


def insert():
	"""Inserts values into an empty space on the grid"""

	n = random.randint(0, 10)  #Number from 1 to 10
	#print(n)
	if n == 6:  #Allows for a 10% chance to have a 4 instead of 2
		item = 4
	else:
		item = 2

	numSpaces = len(emptySpaces)

	place = emptySpaces.pop(random.randint(0, numSpaces - 1))
	#print(place), print(place[0]), print(place[1])
	grid[place[0]][place[1]] = item

#############


def show_Grid():
	print()
	print("+----+----+----+----+")

	for i in range(4):

		print("¦{}¦{}¦{}¦{}¦".format(
		 (" " * (4 - len(str(grid[i][0])))) + str(grid[i][0]),
		 (" " * (4 - len(str(grid[i][1])))) + str(grid[i][1]),
		 (" " * (4 - len(str(grid[i][2])))) + str(grid[i][2]),
		 (" " * (4 - len(str(grid[i][3])))) + str(grid[i][3])))

		print("+----+----+----+----+")

#	print("+----+----+----+----+")
#	print("¦{}¦{}¦{}¦{}¦".format((" "*(4-len(str(grid[0][0])))) +  str(grid[0][0]), (" "*(4-len(str(grid[0][1])))) +  str(grid[0][1]), (" "*(4-len(str(grid[0][2])))) +  str(grid[0][2]), (" "*(4-len(str(grid[0][3])))) +  str(grid[0][3])))
#	print("+----+----+----+----+")
#	print("¦{}¦{}¦{}¦{}¦".format((" "*(4-len(str(grid[1][0])))) +  str(grid[1][0]), (" "*(4-len(str(grid[1][1])))) +  str(grid[1][1]), (" "*(4-len(str(grid[1][2])))) +  str(grid[1][2]), (" "*(4-len(str(grid[1][3])))) +  str(grid[1][3])))
#	print("+----+----+----+----+")
#	print("¦{}¦{}¦{}¦{}¦".format((" "*(4-len(str(grid[2][0])))) +  str(grid[2][0]), (" "*(4-len(str(grid[2][1])))) +  str(grid[2][1]), (" "*(4-len(str(grid[2][2])))) +  str(grid[2][2]), (" "*(4-len(str(grid[2][3])))) +  str(grid[2][3])))
#	print("+----+----+----+----+")
#	print("¦{}¦{}¦{}¦{}¦".format((" "*(4-len(str(grid[3][0])))) +  str(grid[3][0]), (" "*(4-len(str(grid[3][1])))) +  str(grid[3][1]), (" "*(4-len(str(grid[3][2])))) +  str(grid[3][2]), (" "*(4-len(str(grid[3][3])))) +  str(grid[3][3])))
#	print("+----+----+----+----+")


########__MAIN__########

# 	ORDER
#	Check Grid
#	Shift
#	Combine
#	Insert

size = 4
make_Grid(size)

check_Grid()
insert()
show_Grid()

while True:
	check_Grid()
	shift()
	insert()
	show_Grid()
