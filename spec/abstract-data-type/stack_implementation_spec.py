from ivoire import describe, context
from expects import expect
from src.abstract_data_type.stack_implementation import Stack
from src.abstract_data_type.stack_interface import StackInterface

with describe(Stack) as it:
  @it.before
  def before(test):
    test.stack = Stack()

  @it.after
  def after(test):
    # is it necessary?
    test.stack = None

  with it('inherits from StackInterface') as test:
      expect(test.stack).to.be.a(StackInterface)

  with context(Stack.__init__):
    with it('create an empty stack') as test:
      expect(test.stack.items).to.be.empty

  with context(Stack.push):
    with it('add a new item to the end of the stack') as test:
      item = 4
      test.stack.push(item)
      last_item = test.stack.items[-1]
      
      expect(last_item).to.be(item)

  with context(Stack.pop):
    with it('remove and return the last added item from the stack') as test:
      item = 4
      test.stack.push(item)
      last_item = test.stack.pop()
      
      expect(last_item).to.be(item)

  with context(Stack.isEmpty):
    with it('return true if the stack is empty') as test:
      expect(test.stack.isEmpty()).to.be.true