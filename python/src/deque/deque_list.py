from deque_interface import DequeInterface

class DequeList(DequeInterface):
	""" implementation of a deque using a python list """

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return (self.items == [])

	def insertFirst(self, item):
		self.items.insert(0, item)

	def insertLast(self, item):
		self.items.append(item)

	def removeFirst(self):
		return self.items.pop(0)

	def removeLast(self):
		return self.items.pop()

	def size(self):
		return len(self.items)
