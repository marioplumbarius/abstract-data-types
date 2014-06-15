from queue_adt import QueueADT
from src.linked_lists.node import Node

class LinkedQueue(QueueADT):
  """ 
    *FIFO policy
  implementation of the Queue ADT, made up of linked Node objects
  """
  def __init__(self):
    self.length = 0
    self.head = None

  """ identical to LinkedList's one """
  def isEmpty(self):
    return (self.length == 0)

  """ a bit more complicated than LinkedList's one """
  def insert(self, cargo):
    # takes linear time
    node = Node(cargo)
    node.next = None

    if self.head == None:
      self.head = node
    else:
      last = self.head
      while last.next: last = last.next
      last.next = node
    self.length = self.length + 1

  """ identical to LinkedList's one """
  def remove(self):
    # takes constant time
    cargo = self.head.cargo
    self.head = self.head.next
    self.length = self.length - 1
    return cargo