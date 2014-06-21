from stack_interface import StackInterface

class StackList(StackInterface):
  """ a stack implementation using python lists """

  def __init__(self):
    self.items = []

  def push(self, new_item):
    self.items.append(new_item)

  def pop(self):
    return self.items.pop()

  def isEmpty(self):
    return (self.items == [])