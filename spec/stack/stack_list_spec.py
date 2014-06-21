from ivoire import describe, context
from expects import expect
from src.stack.stack_list import StackList
from src.stack.stack_interface import StackInterface

with describe(StackList) as it:
  @it.before
  def before(test):
    test.stack = StackList()

  with it('inherits from StackInterface') as test:
      expect(test.stack).to.be.a(StackInterface)

  with context(StackList.__init__):
    with it('create an empty stack') as test:
      expect(test.stack.items).to.be.empty

  with context(StackList.push):
    with it('add a new item to the end of the stack') as test:
      item = 4
      test.stack.push(item)
      last_item = test.stack.items[-1]
      
      expect(last_item).to.be(item)

  with context(StackList.pop):
    with it('remove and return the last added item from the stack') as test:
      item = 4
      test.stack.push(item)
      last_item = test.stack.pop()
      
      expect(last_item).to.be(item)

  with context(StackList.isEmpty):
    with it('return true if the stack is empty') as test:
      expect(test.stack.isEmpty()).to.be.true