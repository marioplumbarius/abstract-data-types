from ivoire import describe, context
from expects import expect
from src.stack.stack_linked_list import StackLinkedList
from src.stack.stack_interface import StackInterface
from src.list.node import Node

with describe(StackLinkedList) as it:
  @it.before
  def before(test):
    test.stack = StackLinkedList()

  with it('inherits from StackInterface') as test:
    expect(test.stack).to.be.a(StackInterface)

  with context(StackLinkedList.__init__):
    with it('creates an empty stack') as test:
      expect(test.stack).to.have.property('head', None)
      expect(test.stack).to.have.property('length', 0)

  with context(StackLinkedList.push):
    with it('add a new node at the top of the stack') as test:
      test.stack.push(3)
      test.stack.push(2)
      expect(test.stack.head).to.equal(Node(2))

    with it('increments the length of the stack') as test:
      test.stack.push(4)
      expect(test.stack).to.have.property('length', 1)

    with it('links the next node of the new node to the current head node, when stack is not empty') as test:
      test.stack.push(5)
      test.stack.push(6)
      expect(test.stack.head.next).to.equal(Node(5))

    # TODO: implement me!
    # with it('raises on attempt to add an array as a cargo') as test:
    #   expect(test.stack.push([1,2,3])).to.raise_error(ValueError)


  with context(StackLinkedList.pop):
    with it('remove and return the last added node from the stack') as test:
      test.stack.push(7)
      test.stack.push(77)
      test.stack.push(777)
      expect(test.stack.pop()).to.equal(Node(777))

    with it('raises IndexError on attempt to pop an empty stack') as test:
      expect(test.stack.pop).to.raise_error(IndexError)

    with it('decrements the length os the stack') as test:
      test.stack.push(1)
      test.stack.push(11)
      test.stack.push(11)
      test.stack.pop()
      expect(test.stack).to.have.property('length', 2)

    with it('move the next node to the top of the stack') as test:
      test.stack.push(33)
      test.stack.push(66)
      test.stack.pop()
      expect(test.stack.head).to.equal(Node(33))

  with context(StackLinkedList.isEmpty):
    with it('returns true when stack is empty') as test:
      expect(test.stack.isEmpty()).to.be.true

    with it('returns false when stack is not empty') as test:
      test.stack.push(2)
      expect(test.stack.isEmpty()).to.be.false