from stack_interface import StackInterface

class StackList(StackInterface):
  """ a stack implementation using a python list """

  def __init__(self):
    """ create an empty stack """
    self.items = []

  def push(self, new_item):
    """ add a new item to the stack """
    self.items.append(new_item)

  def pop(self):
    """ remove and return the last added item from the stack """
    return self.items.pop()

  def isEmpty(self):
    """ check is the stack is empty """
    return (self.items == [])
