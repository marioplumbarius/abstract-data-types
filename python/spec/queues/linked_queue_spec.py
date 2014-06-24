from ivoire import describe, context
from expects import expect
from src.queues.linked_queue import LinkedQueue

with describe(LinkedQueue) as it:
  @it.before
  def before(test):
    test.queue = LinkedQueue()

  @it.after
  def after(test):
    test.queue = None

  with context(LinkedQueue.__init__):
    with it('creates an empty queue') as test:
      expect(test.queue).to.have.property('length', 0)
      expect(test.queue).to.have.property('head', None)

  with context(LinkedQueue.isEmpty):
    with it('return true if the queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true

    with it('returns false if the queue is not empty') as test:
      test.queue.insert(7)
      expect(test.queue.isEmpty()).to.be.false

  with context(LinkedQueue.insert):
    with it('add node at the end of the queue') as test:
      test.queue.insert(1)
      test.queue.insert(2)
      test.queue.insert(7)
      expected_cargo = 7
      last_node = test.queue.head

      while last_node.next != None:
        last_node = last_node.next

      expect(last_node.cargo).to.equal(expected_cargo)

    with it('add node at the top/head of the queue when it is empty') as test:
      expected_cargo = 9
      test.queue.insert(expected_cargo)

      expect(test.queue.head.cargo).to.equal(expected_cargo)

    with it('increments the length of the queue') as test:
      test.queue.insert(1)
      expect(test.queue).to.have.property('length', 1)

  with context(LinkedQueue.remove):
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