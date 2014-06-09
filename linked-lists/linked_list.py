from node import Node

class LinkedList():

  """
  A data structure that implements a collection using a sequence of linked nodes.
  """

  def __init__(self):
    self.length = 0
    self.head = None

  def printList(self, sorting_order=1):
    print '[',

    if sorting_order > 0:
      self.printReverse()
    else:
      self.printNormal(self.head)

    print ']',

  def printReverse(self):
    node = self.head
    while node:
      print node
      node = node.next

  def printNormal(self, list):
    if list.next != None:
      tail = list.next
      self.printBackward(tail)
    print list.cargo, ',',

  def addNode(self, cargo):
    if cargo == None: return
    
    node = Node(cargo)
    
    if not self.isEmpty():
      node.next = self.head

    self.head = node
    self.length = self.length + 1

  def isEmpty(self):
    return (self.length == 0)