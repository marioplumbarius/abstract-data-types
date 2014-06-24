from ivoire import describe, context
from expects import expect
from src.queues.linked_queue_improved import LinkedQueueImproved
from src.queues.queue_interface import QueueInterface

with describe(LinkedQueueImproved) as it:
  @it.before
  def before(test):
    test.queue = LinkedQueueImproved()

  with it('inherits from QueueInterface') as test:
    expect(test.queue).to.be.a(QueueInterface)

  with context(LinkedQueueImproved.__init__):
    with it('creates an empty queue') as test:
      expect(test.queue).to.have.property('length', 0)
      expect(test.queue).to.have.property('head', None)
      expect(test.queue).to.have.property('tail', None)

  with context(LinkedQueueImproved.isEmpty):
    with it('returns True when queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true

    with it('returns False when queue is not empty') as test:
      test.queue.insert(88)
      expect(test.queue.isEmpty()).to.be.false

  with context(LinkedQueueImproved.insert):
    with it('adds a new node to the end/tail of the queue') as test:
      test.queue.insert(11)
      test.queue.insert(22)
      expect(test.queue.tail.cargo).to.equal(22)

    with it('increments the queue length') as test:
      test.queue.insert(33)
      expect(test.queue).to.have.property('length', 1)

    with it('when the queue is empty, the new node is assigned both to the head and tail') as test:
      test.queue.insert(55)
      expect(test.queue.head.cargo).to.equal(55)
      expect(test.queue.tail.cargo).to.equal(55)

  with context(LinkedQueueImproved.remove):
    with it('removes and returns the top/head node from the queue') as test:
      test.queue.insert(33)
      test.queue.insert(22)
      topNode = test.queue.head
      expect(test.queue.remove()).to.be(topNode.cargo)

    with it('sets the queue head to the deleted"s next node') as test:
      test.queue.insert(33)
      test.queue.insert(22)
      toBeDeletedNextNode = test.queue.head.next
      test.queue.remove()
      expect(test.queue).to.have.property('head', toBeDeletedNextNode)

    with it('decrements the queue length') as test:
      test.queue.insert(11)
      test.queue.insert(13)
      test.queue.remove()
      expect(test.queue).to.have.property('length', 1)

    with it('when the last node is removed, sets its tail to None') as test:
      for x in xrange(3):
        test.queue.insert(x)
      while not test.queue.isEmpty(): test.queue.remove()
      expect(test.queue).to.have.property('length', 0)

    with it('returns None when queue is empty') as test:
      expect(test.queue.remove()).to.be.none