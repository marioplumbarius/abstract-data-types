class Tree():
  """ implementation of a tree """

  def __init__(self, cargo, left=None, right=None):
    """ create a tree """
    # can be any type
    self.cargo = cargo
    # should be also tree nodes
    self.left = left
    self.right = right

  def __str__(self):
    """ representation of a tree: tree.cargo """
    return str(self.cargo)

  def getCargo(self):
    """ return the cargo of the tree """
    return self.cargo

  def getLeft(self):
    """ return the left node of the tree """
    return self.left

  def getRight(self):
    """ return the right node of the tree """
    return self.right

  def setLeft(self, left):
    """ set the left node of the tree """
    self.left = left

  def setRight(self, right):
    """ set the right node of the tree """
    self.right = right

  def setCargo(self, cargo):
    """ set the cargo of the tree """
    self.cargo = cargo

  @classmethod
  def total(self, tree):
    """ recursively sums the total cargos of a tree """
    if tree == None: return 0
    return  tree.cargo + \
            Tree.total(tree.left) + \
            Tree.total(tree.right)