from stack_interface import StackInterface
""" 
  an implementation is a set of methods that satisfy the syntactic and semantic requirements of an interface.
"""

class Stack(StackInterface):
  """
    - ageneric data structure:
        we can add any type of item to it
    - a veneer:
        in which the methods consist of simple invocations of existing methods
  """

  def __init__(self):
    self.items = []

  def push(self, new_item):
    self.items.append(new_item)

  def pop(self):
    return self.items.pop()

  def isEmpty(self):
    return (self.items == [])