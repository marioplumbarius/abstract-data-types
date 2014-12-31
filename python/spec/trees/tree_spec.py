from ivoire import describe, context
from expects import expect
from src.trees.tree import Tree

with describe(Tree) as it:
    @it.before
    def before(test):
        test.defaultCargo = 2.22
        test.tree = Tree(test.defaultCargo)

    with context(Tree.__init__):
        with it('creates a new tree with a cargo value') as test:
            expect(test.tree).to.have.property('cargo', test.defaultCargo)

        with it('creates a new tree with an empty left node') as test:
            expect(test.tree).to.have.property('left', None)

        with it('creates a new tree with an empty right node') as test:
            expect(test.tree).to.have.property('right', None)

    with context(Tree.__str__):
        with it('returns the representation of the tree: its cargo') as test:
            expect(test.tree.__str__()).to.equal(str(test.tree.cargo))

    with context(Tree.getCargo):
        with it('returns the cargo of the tree') as test:
            expect(test.tree.getCargo()).to.equal(test.tree.cargo)

    with context(Tree.getLeft):
        with it('returns the left node of the tree') as test:
            leftTreeNode = Tree(22)
            rightTreeNode = Tree(11)

            test.tree.setLeft(leftTreeNode)
            test.tree.setRight(rightTreeNode)

            expect(test.tree.getLeft()).to.equal(leftTreeNode)

    with context(Tree.getRight):
        with it('returns the right node of the tree') as test:
            leftTreeNode = Tree(22)
            rightTreeNode = Tree(11)

            test.tree.setLeft(leftTreeNode)
            test.tree.setRight(rightTreeNode)

            expect(test.tree.getRight()).to.equal(rightTreeNode)

    with context(Tree.setLeft):
        with it('sets the left node of the tree') as test:
            leftTreeNode = Tree(22)
            rightTreeNode = Tree(11)

            test.tree.setLeft(leftTreeNode)
            test.tree.setRight(rightTreeNode)

            expect(test.tree.left).to.equal(leftTreeNode)

    with context(Tree.setRight):
        with it('sets the right node of the tree') as test:
            leftTreeNode = Tree(22)
            rightTreeNode = Tree(11)

            test.tree.setLeft(leftTreeNode)
            test.tree.setRight(rightTreeNode)

            expect(test.tree.right).to.equal(rightTreeNode)

    with context(Tree.setCargo):
        with it('sets the cargo of the tree') as test:
            newCargoValue = 55

            test.tree.setCargo(newCargoValue)

            expect(test.tree.cargo).to.equal(newCargoValue)

    with context(Tree.total):
        with it('returns 0 when no tree is passed as argument') as test:
            expect(Tree.total(None)).to.equal(0)

        with it('recursively sums the total cargos of a tree') as test:
            cargos = [1,2,3,4, test.defaultCargo]
            totalSumCargos = sum(cargos)
            tree1 = Tree(cargos[0])
            tree2 = Tree(cargos[1])
            tree3 = Tree(cargos[2], tree1)
            tree4 = Tree(cargos[3], tree2)

            test.tree.setLeft(tree3)
            test.tree.setRight(tree4)

            expect(Tree.total(test.tree)).to.equal(totalSumCargos)