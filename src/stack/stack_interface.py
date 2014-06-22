class StackInterface():
  """ interface for a stack adt: LIFO policy """

  def __init__(self):
    """ initialize a new empty stack """
    raise "StackInterface.__init is not implemented"

  def push(self, new_item):
    """ add a new item to the stack """
    raise "StackInterface.push is not implemented"

  def pop(self):
    """ remove and return the last added item from the stack """
    raise "StackInterface.pop is not implemented"

  def isEmpty(self):
    """ check whether the stack is empty """
    raise "StackInterface.isEmpty is not implemented"
