from queue_adt import QueueADT
from node import Node

class QueueList(QueueADT):
  def __init__(self):
    self.length = 0
    self.list = []

  def isEmpty(self):
    return (self.length == 0)

  def insert(self, cargo):
    node = Node(cargo)
    node.next = None
    
    self.list.append(node)
    self.length = self.length + 1

  def remove(self):
    if self.length == 0: return
    self.length = self.length - 1
    return self.list.pop(0)