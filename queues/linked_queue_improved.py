from queue_adt import QueueADT
from node import Node

class LinkedQueueImproved(QueueADT):
  def __init__(self):
    self.length = 0
    self.head = None
    self.last = None

  def isEmpty(self):
    return (self.length == 0)

  def insert(self, cargo):
    # now, constant time!
    node = Node(cargo)
    node.next = None

    if self.length == 0:
      self.head = self.last = node
    else:
      last = self.last
      last.next = node
      self.last = node
    self.length = self.length + 1

  def remove(self):
    cargo = self.head.cargo
    self.head = self.head.next
    self.length = self.length - 1
    if self.length == 0:
      self.last = None
    return cargo