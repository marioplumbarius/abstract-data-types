from deque_interface import DequeInterface

class DequeList(DequeInterface):
	""" implementation of a deque using a python list """

	def __init__(self):
		""" create an empty deque """
		self.items = []

	def isEmpty(self):
		""" check if the deque is empty """
		return (self.items == [])

	def insertFirst(self, item):
		""" add an item at the top of the deque """
		self.items.insert(0, item)

	def insertLast(self, item):
		""" add an item at the end of the deque """
		self.items.append(item)

	def removeFirst(self):
		""" remove and return the item at the top of the deque """
		return self.items.pop(0)

	def removeLast(self):
		""" remove and return the item at the end of the deque """
		return self.items.pop()

	def size(self):
		""" return the length of the deque """
		return len(self.items)
