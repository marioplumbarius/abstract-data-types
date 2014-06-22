class Node():
  """ object that contains a reference to another object of the same type """
  
  def __init__(self, cargo=None, next=None):
    self.cargo = cargo # An item of data contained in a node.
    self.next = next

  def __str__(self):
    return str(self.cargo)

  def __cmp__(self, other):
    if not isinstance(other, Node): return -1
    if self.cargo > other.cargo: return 1
    elif self.cargo < other.cargo: return -1
    return 0