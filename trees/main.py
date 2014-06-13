"""
  Trees
  - made up of nodes.. also contains cargo
  - recursive data structure
  - a node that contains an object referente and two three references

  examples:
  - binary tree: each node contains a reference to two other nodes. These references are referred to as the left and right subtrees

  GRAMMAR
    root = top of the tree
    other nodes = branches
    leaves = nodes at the tips with null references
    parent = top node
    children = nodes the parent refers to
    siblings = nodes with the same parent
    level = nodes that are in the same distance from the root node, comprise a level of the tree

    INTERESTING
    Expression trees have many uses. The example in this chapter uses trees to translate expressions to postfix, prefix, and infix. Similar trees are used inside compilers to parse, optimize, and translate programs.
"""


""" building a tree from bottom up """
from tree import Tree, total
import cProfile

left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)
# cProfile.run('total(tree)')

""" expression trees """
# representing the computation unambiguously of 1 + 2 * 3 (=> infix notation)
exp_tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

""" tree traversal """
from printing_trees import printTreePreorder, printTreePostorder, printTreeInorder, printTreeIndented
printTreePreorder(tree)
print total(tree)
# prefix notation
printTreePreorder(exp_tree)
print
# postfix notation
printTreePostorder(exp_tree)
print
# infix notation
printTreeInorder(exp_tree)
print
# keeping track of level to improve the output
printTreeIndented(exp_tree)
"""
output:
      3   => 2 levels from the root (sibling to 2)
  *       => 1 level from the root (sibling to 1)
    2     => 2 levels from the root (sibling to 3)
+         => root
  1       => 1 level from the root (sibling to *)
"""

print
""" computing expression trees """
from expression_trees import compute
def compute_and_print_trees(exps):
  for exp in exps:
    tree = compute(exp)
    printTreePostorder(tree)
    print

exps_valid = [
  '9+1',
  '9*1',
  '9*1+5',
  '9*(1+5)',
  '9*(1+5)*7'
]

compute_and_print_trees(exps_valid)