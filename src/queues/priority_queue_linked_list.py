from src.linked_lists.node import Node
from priority_queue_adt import PriorityQueueADT

class PQLinkedList(PriorityQueueADT):
  def __init__(self):
    self.length = 0
    self.head = None

  def isEmpty(self):
    return (self.length == 0)

  def insert(self, item):
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

  def printList(self):
    item = self.head
    print '[',
    while item:
      print item,
      item = item.next

      if item: print ',',

    print ']',

  def remove(self):
    item = self.head
    self.head = self.head.next
    self.length = self.length - 1
    return item