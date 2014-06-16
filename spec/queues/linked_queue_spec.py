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
    with it('set the length of the queue to zero') as test:
      expect(test.queue).to.have.property('length', 0)

    with it('set the head of the queue to None') as test:
      expect(test.queue).to.have.property('head', None)

  with context(LinkedQueue.isEmpty):
    with it('return true if the queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true

  with context(LinkedQueue.insert):
    with it('add a new node at the end of the queue') as test:
      test.queue.insert(1)
      test.queue.insert(2)
      test.queue.insert(7)
      expected_cargo = 7
      last_node = test.queue.head

      while last_node.next != None:
        last_node = last_node.next

      expect(last_node.cargo).to.be(expected_cargo)

    with it('add a new node at the top/head of the queue when it is empty') as test:
      expected_cargo = 9
      test.queue.insert(expected_cargo)

      expect(test.queue.head.cargo).to.be(expected_cargo)

    with it('increments the length of the queue when a new node is added') as test:
      test.queue.insert(1)
      expect(test.queue.length).to.be(1)

    with it('raise on attempt to add a cargo with a None value') as test:

      def callback():
        test.queue.insert()

      expect(callback).to.raise_error(TypeError)