class Helper():
  """ temporary python list helper class """

  @classmethod
  def remove_item_from_list_at_index(self, items, index):
    """ remove an element at the given index from the list """
    items[index:index+1] = []

  @classmethod
  def get_max_item_index(self, items):
    """ find and return the index of the element with the max value """
    maxi = 0
    for i in range(1, len(items)):
      if items[i] > items[maxi]:
        maxi = i
    return maxi