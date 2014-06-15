"""
  Let's take a look at two ADTs:
  - Queue ADT (FIFO)
  - Priority Queue ADT (priority)

  Real life examples:
  - in most cases, the first customer in line is the next customer to be served
  - at supermarkets, a customer with only a few items go FIRST
  - at airports, customers whose flights are leaving soon are taken from the middle of the queue

  queueing policy
  - the rule that determines who goes next
  - e.g.: FIFO, LIFO, priority queueing

  priority queueing
  - each customer is assigned a priority and the customer with the highest priority goes first, regardless of the order of arrival

"""

""" Queue """

""" playing with time complexity """
import cProfile
from linked_queue import LinkedQueue
from linked_queue_improved import LinkedQueueImproved
from queue_list import QueueList

""" implementation of a queue adt which inserts takes linear time.. bad solution =/ """
def run_linked_queue():
  a = LinkedQueue()
  for x in range(0,1000):
    a.insert(x)

""" implementation of a queue adt which inserts takes constant time.. good solution =/ """
def run_improved_queue():
  b = LinkedQueueImproved()
  for y in range(0,1000):
    b.insert(y)

""" implementation of a queue adt using python list """
def run_queue_list():
  c = QueueList()
  for z in range(0,1000):
    c.insert(z)

# cProfile.run('run_linked_queue()') # ~0.6s
# cProfile.run('run_improved_queue()') # ~0.03s
# cProfile.run('run_queue_list()') # ~0.02


""" Priority Queue"""
from priority_queue import PriorityQueue
from cmp_example import Golfer
from priority_queue_linked_list import PQLinkedList
import random

""" implementation of a priority queue adt using python list """
def run_priority_queue():
  q = PriorityQueue() 
  for w in range(1,1000):
    q.insert(w)
  while not q.isEmpty(): q.remove()

""" same implementation as above, just to demonstrate how cmp works for comparison """
def run_priority_queue_cmp():
  tiger = Golfer('Tiger woods', 61)
  phil = Golfer('Phil mickelson', 72)
  hal = Golfer('Hal sutton', 69)

  pq = PriorityQueue()
  pq.insert(tiger)
  pq.insert(phil)
  pq.insert(hal)

  while not pq.isEmpty(): pq.remove()

""" implementation of a prioriry queue adt using a linked list  """
def run_priority_queue_linked_list():
  l = PQLinkedList()
  for i in range(1,100):
    rand = int(random.random()*100)
    l.insert(rand)
  
  while not l.isEmpty(): l.remove()

# cProfile.run('run_priority_queue()')
# cProfile.run('run_priority_queue_cmp()')
# cProfile.run('run_priority_queue_linked_list()')