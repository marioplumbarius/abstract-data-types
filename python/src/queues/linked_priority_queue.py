from src.list.node import Node
from priority_queue_interface import PriorityQueueInterface

class PriorityQueueLinkedList(PriorityQueueInterface):
  """ implementation of an ordered priority queue using a linked list """
  
  def __init__(self):
    """ create an empty queue """
    self.length = 0
    self.head = None

  def isEmpty(self):
    """ check if the queue is empty """
    return (self.length == 0)

  def insert(self, item):
    """ add a new node at the the queue """
    node = Node(item)

    if self.isEmpty():
      self.head = node
    else:
      if node > self.head:
        node.next = self.head
        self.head = node
      else:
        tail = self.head
        last = tail
        while tail:
          if tail > node:
            last = tail
            tail = tail.next
            
            if tail < node: break
          else:
            return

        node.next = tail
        last.next = node

    self.length = self.length + 1

  # TODO: spec me
  def printList(self):
    """ print the whole queue """
    item = self.head
    print '[',
    while item:
      print item,
      item = item.next

      if item: print ',',

    print ']',

  def remove(self):
    """ remove and return the node at the top of the queue"""
    item = self.head
    self.head = self.head.next
    self.length = self.length - 1
    return item