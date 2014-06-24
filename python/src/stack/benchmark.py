from stack_linked_list import StackLinkedList
from stack_list import StackList
import cProfile

def createStack(Klass):
  s = Klass()
  for x in xrange(200000):
    s.push(x)

  return s

stack_list = createStack(StackList)
stack_linked_list = createStack(StackLinkedList)

def traverseStack(stack):
  while not stack.isEmpty(): return stack.pop()

# cProfile.run('createStack(StackList)')
# cProfile.run('createStack(StackLinkedList)')
# cProfile.run('traverseStack(stack_list)')
# cProfile.run('traverseStack(stack_linked_list)')