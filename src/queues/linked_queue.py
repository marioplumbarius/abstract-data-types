from queue_adt import QueueADT
from src.list.node import Node

class LinkedQueue(QueueADT):
  """ implementation of a queue using a linked list data structure """
  
  def __init__(self):
    """ create an empty queue """
    self.length = 0
    self.head = None

  def isEmpty(self):
    """ check if the queue is empty """
    return (self.length == 0)

  def insert(self, cargo):
    """ insert a new node at the end of the queue: O(n) """
    node = Node(cargo)
    node.next = None

    if self.head == None:
      self.head = node
    else:
      last = self.head
      while last.next: last = last.next
      last.next = node
    self.length = self.length + 1

  def remove(self):
    """ remove and return the node at the top of the queue: O(1) """
    if self.isEmpty(): return
    cargo = self.head.cargo
    self.head = self.head.next
    self.length = self.length - 1
    return cargo