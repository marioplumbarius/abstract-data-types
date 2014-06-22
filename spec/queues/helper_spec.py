from ivoire import describe, context
from expects import expect
from src.queues.helper import Helper

with describe(Helper) as it:
  @it.before
  def before(test):
    test.list = [22,100,2,98,0]
  
  with context(Helper.remove_item_from_list_at_index):
    with it('remove an element from a list at the given index') as test:
      Helper.remove_item_from_list_at_index(test.list, 2)
      expect(test.list[2]).to.equal(98)

  with context(Helper.get_max_item_index):
    with it('find and return the index of the element with the max value in the list') as test:
      expect(Helper.get_max_item_index(test.list)).to.equal(1)