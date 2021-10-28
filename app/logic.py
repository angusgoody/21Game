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

	# For now just return the next two numbers
	return [score + 1, score + 2]
