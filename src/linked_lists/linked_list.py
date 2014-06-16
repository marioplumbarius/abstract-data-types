from node import Node

class LinkedList():

  """
  A data structure that implements a collection using a sequence of linked nodes.
  """

  def __init__(self):
    self.length = 0
    self.head = None

  # TODO: spec me
  def printList(self, sorting_order=1):
    print '[',

    if sorting_order > 0:
      self.printBackward(self.head)
    else:
      self.printFoward(self.head)

    print ']',

  # TODO: spec me
  def printFoward(self, node):
    if node != None:
      print node,
      node = node.next
      if node: print ',',
      self.printFoward(node)

  # TODO: spec me
  def printBackward(self, node):
    if node.next != None:
      tail = node.next
      self.printBackward(tail)
      print ',',
    print node.cargo,

  def addNode(self, cargo):
    if cargo == None: return
    
    node = Node(cargo)
    
    if not self.isEmpty():
      node.next = self.head

    self.head = node
    self.length = self.length + 1

  def isEmpty(self):
    return (self.length == 0)