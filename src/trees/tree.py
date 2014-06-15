class Tree():
  def __init__(self, cargo, left=None, right=None):
    # can be any type
    self.cargo = cargo
    # should be also tree nodes
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.cargo)

  def getCargo(self):
    return self.cargo

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def setLeft(self, left):
    self.left = left
  
  def setRight(self, right):
    self.right = right

  def setCargo(self, cargo):
    self.cargo = cargo  

def total(tree):
  if tree == None: return 0
  return  tree.cargo + \
          total(tree.left) + \
          total(tree.right)