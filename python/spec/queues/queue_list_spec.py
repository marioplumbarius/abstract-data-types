from ivoire import describe, context
from expects import expect
from src.queues.queue_list import QueueList
from src.queues.queue_interface import QueueInterface

with describe(QueueList) as it:
  @it.before
  def before(test):
    test.queue = QueueList()

  with it('inherits from the QueueInterface') as test:
    expect(test.queue).to.be.a(QueueInterface)

  with context(QueueList.__init__):
    with it('creates an empty queue') as test:
      expect(test.queue.list).to.be.empty

  with context(QueueList.isEmpty):
    with it('returns true when queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true

    with it('returns false when queue is not empty') as test:
      test.queue.insert(1)
      expect(test.queue.isEmpty()).to.be.false

  with context(QueueList.insert):
    with it('adds a new node at the end of the queue') as test:
      test.queue.insert(2)
      test.queue.insert(3)
      expect(test.queue.list[-1].cargo).to.equal(3)

  with context(QueueList.remove):
    with it('removes and returns the node at the top of the queue') as test:
      test.queue.insert(4)
      test.queue.insert(5)
      expect(test.queue.remove().cargo).to.equal(4)