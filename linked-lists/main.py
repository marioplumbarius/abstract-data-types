"""
A linked list is:
  - recursive data structure
  - have nodes
  - that have cargos (unit of data)
"""

# LINKED_NODES
from node import Node

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3
n3.next = None

"""
And we got this representation:
  n1.cargo = 1, n1.next = n2
  n2.cargo = 2, n2.next = n3
  n3.cargo = 3, n3.next = None

!! the first node of the list serves as a reference to the entire list
"""

# PRINTING
def printList(node):
  print '[',
  while node:
    print node,
    node = node.next
    if node: print ',', 
  print ']'

printList(n1)

def printListBackward(node):
  # recursive
  if node == None: return
  head = node
  tail = node.next
  printListBackward(tail)
  print head,

printListBackward(n1)
print

# MODIFYING LISTS
def removeSecond(list):
  if list == None: return
  first = list
  
  if list.next == None: return
  
  second = list.next
  first.next = second.next
  second.next = None
  return second

# usages
print 'removing second node from a list with 3 nodes'
printList(n1)
removed = removeSecond(n1)
print 'removed node', printList(removed)

print 'removing second node from a list with only 1 node'
printList(removed)
removed = removeSecond(removed)
print 'removed node', printList(removed)

print 'removing second node from a empty list'
printList(removed)
removed = removeSecond(removed)
print 'removed node', printList(removed)