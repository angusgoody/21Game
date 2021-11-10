import unittest
from app import logic


class PlayTests(unittest.TestCase):
	"""
	Test the Play functionality in the logic
	file
	"""

	def test1(self):
		self.assertEqual(logic.playMove(3, 3), [4, 5, 6])

	def test2(self):
		self.assertEqual(logic.playMove(3, 18), [19, 20])

	def test3(self):
		self.assertEqual(logic.playMove(3, 20), [21])

	def test4(self):
		self.assertEqual(logic.playMove(3, 17), [18,19,20])


class NameTests(unittest.TestCase):
	"""
	Test the name functionality in the logic
	file
	"""

	def get_name(self):
		self.assertEqual(logic.getName(), "Angus")


if __name__ == '__main__':
	unittest.main()
