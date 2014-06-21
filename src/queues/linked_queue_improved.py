from queue_adt import QueueADT
from src.list.node import Node

class LinkedQueueImproved(QueueADT):
  """ implementation of a queue using a linked list data structure """

  def __init__(self):
    """ create an empty queue """
    self.length = 0
    self.head = None
    self.tail = None

  def isEmpty(self):
    """ check if the queue is empty """
    return (self.length == 0)

  def insert(self, cargo):
    """ insert a new node a the end of the queue: O(1) """
    node = Node(cargo)
    node.next = None

    if self.length == 0:
      self.head = self.tail = node
    else:
      tail = self.tail
      tail.next = node
      self.tail = node
    self.length = self.length + 1

  def remove(self):
    """ remove and return the node at the top of the queue: O(1) """
    if self.isEmpty(): return
    cargo = self.head.cargo
    self.head = self.head.next
    self.length = self.length - 1
    if self.length == 0:
      self.tail = None
    return cargo