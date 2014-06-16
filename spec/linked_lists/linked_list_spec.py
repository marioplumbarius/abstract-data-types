from ivoire import describe, context
from expects import expect
from src.linked_lists.linked_list import LinkedList
from src.linked_lists.node import Node

with describe(LinkedList) as it:
  @it.before
  def before(test):
    test.list = LinkedList()

  @it.after
  def after(test):
    test.list = None

  with context(LinkedList.__init__):
    with it('set its length to zero') as test:
      expect(test.list.length).to.be(0)

    with it('set its head to None') as test:
      expect(test.list.head).to.be.none

  with context(LinkedList.isEmpty):
    with it('return true if the list is empty') as test:
      expect(test.list.isEmpty()).to.be.true

  with context(LinkedList.addNode):
    # fixme!!!
    with it('does not add a new item when it is None') as test:
      test.list.addNode(None)
      expect(test.list.head).to.be.none

    with it('create a Node object and add it to the list') as test:
      test.list.addNode(33)
      expect(test.list.head).to.be.a(Node)

    with it('increments the length of the linked list') as test:
      test.list.addNode(22)
      expect(test.list.length).to.be(1)

    with it('the first item added does not link to any item') as test:
      test.list.addNode(33)
      expect(test.list.head.next).to.be.none

    with it('add a item at the top/head of the list') as test:
      test.list.addNode(44)
      expect(test.list.head.cargo).to.be(44)

    with it('link the added item to the head of the list, when list is not empty') as test:
      test.list.addNode(55)
      test.list.addNode(66)
      expect(test.list.head.next.cargo).to.be(55)