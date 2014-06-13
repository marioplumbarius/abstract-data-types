""" using a tree to represent a knowlegge base """
from tree import Tree
from string import lower
from printing_trees import printTreeIndented

def yes(question):
  ans = lower(raw_input(question))
  return (ans[0] == 'y')

def animal():
  # start with a singleton
  root = Tree('bird')

  # loop until the user quits
  while True:
    print
    if not yes('Are you thinking of an animal?\n'): break

    # walk the tree
    tree = root
    # the first time the code is runned, this loop is not executed
    # does I have guesses?
    while tree.getLeft() != None:
      # let's make some assumptions I've just learned
      prompt = tree.getCargo() + '? '
      # if my assumption is correct
      if yes(prompt):
        # let's set the tree to the actual answer the user taught me
        tree = tree.getRight()
      else:
        # if none of my assumptions are correct, let's learn new ones
        # assumptions get stored under left branches
        tree = tree.getLeft()

    # makes a guess
    # let's make a guess, the following returns an animal
    guess = tree.getCargo()
    prompt = 'Is it a %s ?' % guess
    if yes(prompt):
      # if i am correct, let's celebrate!
      print 'I rule!'
      continue

    # get new information
    # this question capture the animal name I will use as a guess in the future
    prompt = 'What is the animal\'s name?'
    animal = raw_input(prompt)
    # this one, capture the question I'm going to ask before guess the above animal
    prompt = 'What question would distinguish a %s from a %s? '
    question = raw_input(prompt % (animal, guess))

    # add new information to the tree
    # let me set the question I've just learned
    tree.setCargo(question)
    # and let's found out what would be the answer for that animal
    prompt = 'If the animal were %s the answer would be? '
    guess_tree = Tree(guess)
    animal_tree = Tree(animal)
    # depending on the user's feedback, we store:
    if yes(prompt % animal):
      # the guess on the left, for positive response
      tree.setLeft(guess_tree)
      # the guess on the right, for negative response
      tree.setRight(animal_tree)
    else:
      # the same here
      tree.setLeft(animal_tree)
      tree.setRight(guess_tree)
  printTreeIndented(root)

# animal()
"""
  TODO
  As an exercise, think of various ways you might save the knowledge tree in a file. Implement the one you think is easiest.
"""