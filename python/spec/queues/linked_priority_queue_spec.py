from ivoire import describe, context
from expects import expect
from src.queues.linked_priority_queue import PriorityQueueLinkedList
from src.queues.priority_queue_interface import PriorityQueueInterface
from src.list.node import Node

with describe(PriorityQueueLinkedList) as it:
  @it.before
  def before(test):
    test.queue = PriorityQueueLinkedList()

  with it('inherits from PriorityQueueInterface') as test:
    expect(test.queue).to.be.a(PriorityQueueInterface)

  with context(PriorityQueueLinkedList.__init__):
    with it('creates an empty queue') as test:
      expect(test.queue).to.have.property('length', 0)
      expect(test.queue).to.have.property('head', None)

  with context(PriorityQueueLinkedList.insert):
    with it('when queue is empty, add a node at the top of the queue') as test:
      test.queue.insert(100)
      expect(test.queue).to.have.property('head', Node(100))

    with it('increments the length of the queue') as test:
      test.queue.insert(100)
      expect(test.queue).to.have.property('length', 1)

    with it('add a node at the queue in a position based on its priority') as test:
      test.queue.insert(33)
      test.queue.insert(2)
      test.queue.insert(22)

      expect(test.queue.head).to.equal(Node(33))
      expect(test.queue.head.next).to.equal(Node(22))
      expect(test.queue.head.next.next).to.equal(Node(2))

  with context(PriorityQueueLinkedList.remove):
    with it('remove and return the node at the top of the queue') as test:
      test.queue.insert(22)
      test.queue.insert(100)
      test.queue.insert(2)
      expect(test.queue.remove()).to.equal(Node(100))

    with it('decrements the length of the queue') as test:
      test.queue.insert(22)
      test.queue.insert(100)
      test.queue.remove()
      expect(test.queue).to.have.property('length', 1)


  with context(PriorityQueueLinkedList.isEmpty):
    with it('return true when queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true
    with it('return false when queue is not empty') as test:
      test.queue.insert(22)
      expect(test.queue.isEmpty()).to.be.false