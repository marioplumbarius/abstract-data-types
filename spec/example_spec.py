from ivoire import describe, context
from expects import expect


class Calculator(object):
    def multiply(self, x, y):
	return x * y
   
    def add(self, x, y):
        return x + y

    def divide(self, x, y):
        return x / y


with describe(Calculator) as it:
    @it.before
    def before(test):
        print 'it before'
        test.calc = Calculator()

    @it.after
    def after(test):
        print 'it after'
        test.calc = None

    with it("adds two numbers") as test:
        expect(test.calc.add(2,4)).to.equal(1)
        # test.assertEqual(test.calc.add(2, 4), 6)


    with it("multiplies two numbers") as test:
        test.assertEqual(test.calc.multiply(2, 3), 6)

    with context(Calculator.divide):
        with it("divides two numbers") as test:
            test.assertEqual(test.calc.divide(8, 4), 2)

        with it("doesn't divide by zero") as test:
            with test.assertRaises(ZeroDivisionError):
                test.calc.divide(8, 0)