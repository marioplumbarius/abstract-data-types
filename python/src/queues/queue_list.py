from queue_interface import QueueInterface
from src.list.node import Node

class QueueList(QueueInterface):
  """ implementation of a queue using a python list """

  def __init__(self):
    """ create an empty queue """
    self.list = []

  def isEmpty(self):
    """ check if queue is empty """
    return (self.list == [])

  def insert(self, cargo):
    """ add a new node to the queue """
    node = Node(cargo)
    self.list.append(node)

  def remove(self):
    """ remove and return the node at the top of the queue """
    return self.list.pop(0)