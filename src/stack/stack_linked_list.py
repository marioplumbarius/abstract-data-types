from stack_interface import StackInterface
from src.list.node import Node

class StackLinkedList(StackInterface):
  """ stack implementation using a linked list """

  def __init__(self):
    """ create a new empty stack """
    self.head = None
    self.length = 0

  def isEmpty(self):
    """ verify is the stack is empty """
    return (self.length == 0)

  def push(self, cargo):
    """ add a new node to the stack """
    node = Node(cargo)

    if not self.isEmpty():
      node.next = self.head

    self.head = node
    self.length+=1

  def pop(self):
    """ remove and return the last added node from the stack """
    toBeRemoved = self.head
    self.head = self.head.next
    self.length-=1
    return toBeRemoved