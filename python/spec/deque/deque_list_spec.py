from ivoire import describe, context
from expects import expect
from src.deque.deque_list import DequeList
from src.deque.deque_interface import DequeInterface

with describe(DequeList) as it:
    @it.before
    def before(test):
        test.deque = DequeList()

    with it('inherits from the DequeInterface') as test:
        expect(test.deque).to.be.a(DequeInterface)

    with context(DequeList.__init__):
        with it('creates an empty deque') as test:
            expect(test.deque.items).to.be.empty

    with context(DequeList.isEmpty):
        with it('returns true when deque is empty') as test:
            expect(test.deque.isEmpty()).to.be.true

        with it('returns false when deque is not empty') as test:
            test.deque.insertFirst(10)
            test.deque.insertLast(9)

            expect(test.deque.isEmpty()).to.be.false

    with context(DequeList.insertFirst):
        with it('adds an item at the top of the deque') as test:
            items = [11,22,33]
            topItem = items[-1]

            for item in items:
                test.deque.insertFirst(item)

            expect(test.deque.items.pop(0)).to.equal(topItem)

    with context(DequeList.insertLast):
        with it('adds an item at the bottom of the deque') as test:
            items = [11,22,33]
            bottomItem = items[0]

            for item in items:
                test.deque.insertFirst(item)

            expect(test.deque.items.pop()).to.equal(bottomItem)

    with context(DequeList.removeFirst):
        with it('removes an item from the top of the deque') as test:
            items = [11,22,33]
            topItem = items[1]

            for item in items:
                test.deque.insertFirst(item)

            test.deque.removeFirst()

            expect(test.deque.items.pop(0)).to.equal(topItem)

        with it('decrements the size of the deque') as test:
            items = [11,22,33]

            for item in items:
                test.deque.insertFirst(item)

            test.deque.removeFirst()

            expect(test.deque.size()).to.equal(len(items)-1)

        with it('returns the top item of the deque') as test:
            items = [11,22,33]
            topItem = items[-1]

            for item in items:
                test.deque.insertFirst(item)

            expect(test.deque.removeFirst()).to.equal(topItem)

    with context(DequeList.removeLast):
        with it('removes an item from the bottom of the deque') as test:
            items = [11,22,33]
            bottomItem = items[1]

            for item in items:
                test.deque.insertFirst(item)

            test.deque.removeLast()

            expect(test.deque.items.pop()).to.equal(bottomItem)

        with it('decrements the size of the deque') as test:
            items = [11,22,33]

            for item in items:
                test.deque.insertFirst(item)

            test.deque.removeLast()

            expect(test.deque.size()).to.equal(len(items)-1)

        with it('returns the bottom item of the deque') as test:
            items = [11,22,33]
            bottomItem = items[0]

            for item in items:
                test.deque.insertFirst(item)

            expect(test.deque.removeLast()).to.equal(bottomItem)

    with context(DequeList.size):
        with it('returns the length of the deque') as test:
            items = [11,22,33]
            expectedLen = len(items)

            for item in items:
                test.deque.insertFirst(item)

            expect(test.deque.size()).to.equal(expectedLen)