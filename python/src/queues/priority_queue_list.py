from src.list.node import Node
from priority_queue_interface import PriorityQueueInterface
from helper import Helper

class PriorityQueueList(PriorityQueueInterface):
  """ implementation of a priority queue using an unordered python list """

  def __init__(self):
    """ create an empty queue """
    self.items = []

  def isEmpty(self):
    """ check if the queue is empty """
    return (self.items == [])

  def insert(self, item):
    """ add a new item at the end of the queue """
    self.items.append(item)

  def remove(self):
    """ remove and return the item with highest piority from the queue: O(n) """
    maxiIndex = Helper.get_max_item_index(self.items)
    item = self.items[maxiIndex]
    Helper.remove_item_from_list_at_index(self.items, maxiIndex)
    return item