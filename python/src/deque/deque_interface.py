class DequeInterface():
	""" interface of a double-ended queue adt """

	def __init__(self):
		""" create an empty deque """
		raise "DequeInterface.__init__ is not implemented"

	def insertFirst(self, item):
		""" add a new item at the end of the deque """
		raise "DequeInterface.insertFirst is not implemented"
	
	def insertLast(self, item):
		""" add a new item at the top of the deque """
		raise "DequeInterface.insertLast is not implemented"

	def removeFirst(self):
		""" remove and return the item at the top of the deque """
		raise "DequeInterface.removeFirst is not implemented"

	def removeLast(self):
		""" remove and return the item at the end of the deque """
		raise "DequeInterface.removeLast is not implemented"
	
	def isEmpty(self):
		""" check wether the deque is empty """
		raise "DequeInterface.isEmpty is not implemented"

	def size(self):
		""" return the length of the deque """
		raise "DequeInterface.size is not implemented"
