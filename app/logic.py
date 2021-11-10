"""
Logic.py
For declaring functions to use
in the game

26/10/21
"""


def getName():
	"""
	Return the name of the player
	in the game
	:return: Name of player
	"""

	return "Angus"


def playMove(playerCount, score):
	"""
	This function will return the players move
	in a list of up to 3 consecutive numbers
	:param playerCount: Number of players
	:param score: Current score
	:return: List of consecutive numbers
	"""

	target = 20
	diff = target - score
	return consecutive(score,min([1,2,3], key=lambda x:abs(x-diff)))


def consecutive(score,n):
	"""
	This function will return the "n" next
	consecutive numbers after the "score"
	:param score: The current score
	:param n: number of items after score
	:return: list of numbers
	"""
	li = []
	for x in range(n):
		li.append(score+x+1)
	return li