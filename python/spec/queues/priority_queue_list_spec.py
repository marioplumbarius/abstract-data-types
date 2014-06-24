from ivoire import describe, context
from expects import expect
from src.queues.priority_queue_list import PriorityQueueList
from src.queues.priority_queue_interface import PriorityQueueInterface

with describe(PriorityQueueList) as it:
  @it.before
  def before(test):
    test.queue = PriorityQueueList()

  with it('inherits from PriorityQueueInterface') as test:
    expect(test.queue).to.be.a(PriorityQueueInterface)

  with context(PriorityQueueList.__init__):
    with it('creates an empty queue') as test:
      expect(test.queue.items).to.be.empty

  with context(PriorityQueueList.insert):
    with it('add a new item at the end of the queue') as test:
      test.queue.insert(22)
      test.queue.insert(33)
      expect(test.queue.items[-1]).to.equal(33)

  with context(PriorityQueueList.remove):
    with it('remove and return the item with the highest priority from the queue') as test:
      test.queue.insert(55)
      test.queue.insert(8)
      test.queue.insert(100)
      test.queue.insert(22)
      
      def find(items, num):
        for item in items:
          if item == num: return True
        return False

      expect(test.queue.remove()).to.equal(100)
      expect(find(test.queue.items, 100)).to.be.false

  with context(PriorityQueueList.isEmpty):
    with it('returns True when queue is empty') as test:
      expect(test.queue.isEmpty()).to.be.true

    with it('returns False when queue is not empty') as test:
      test.queue.insert(1)
      expect(test.queue.isEmpty()).to.be.false