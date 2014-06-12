from node import Node
from priority_queue_adt import PriorityQueueADT

class PriorityQueue(PriorityQueueADT):
  """ priority queueing policy """

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return (self.items == [])

  def insert(self, item):
    self.items.append(item)

  def remove(self):
    maxi = self.get_max_item_index()
    item = self.items[maxi]
    self.remove_item_from_list(maxi)
    return item

  def remove_item_from_list(self, index):
    self.items[index:index+1] = []

  def get_max_item_index(self):
    maxi = 0
    for i in range(1, len(self.items)):
      if self.items[i] > self.items[maxi]:
        maxi = i
    return maxi