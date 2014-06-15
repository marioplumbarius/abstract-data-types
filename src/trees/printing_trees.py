def printTreePreorder(tree):
  """
    preorder traversing: contents of the root appear before the contents of the children
  """
  if tree == None: return
  print tree.cargo,
  
  printTreePreorder(tree.left)
  printTreePreorder(tree.right)

def printTreePostorder(tree):
  """
    postorder traversing: contents of the subtree appear before the contents of the root
  """
  if tree == None: return  
  printTreePostorder(tree.left)
  printTreePostorder(tree.right)
  print tree.cargo,

def printTreeInorder(tree):
  """
    inorder traversing: contents appear in the order of left tree, root, and then the right tree
  """
  if tree == None: return  
  print '(',
  printTreeInorder(tree.left)
  print '(', tree.cargo, ')',
  printTreeInorder(tree.right)
  print ')',

def printTreeIndented(tree, level=0):
  """
    inorder traversing which keeps track of level to improve the output
  """
  if tree == None: return
  printTreeIndented(tree.right, level+1)
  print '  '*level + str(tree.cargo)
  printTreeIndented(tree.left, level+1)