from ivoire import describe, context
from expects import expect
from src.new_data_type.fraction import Fraction

with describe(Fraction) as it:
  @it.before
  def before(test):
    test.fraction = Fraction(2,3)
    test.other_fraction = Fraction(3,2)
    test.other_int = 3
    test.fraction_equal = Fraction(2,3)
    test.fraction_almost_equal = Fraction(2,4)

  with context(Fraction.__init__):
    
    with it('set the fraction numerator') as test:
      expect(test.fraction.numerator).not_to.be.none

    with it('set the fraction denominator') as test:
      expect(test.fraction.denominator).not_to.be.none

  with context(Fraction.__mul__):
    
    with it('multiply a fraction by another one') as test:
      expect(test.fraction * test.other_fraction).to.equal(Fraction(1,1))
    
    with it('multiply a fraction by an int number') as test:
      expect(test.fraction * test.other_int).to.equal(Fraction(2,1))

    with it('multiply an int number by a fraction') as test:
      expect(test.other_int * test.fraction).to.equal(Fraction(2,1))

  with context(Fraction.__add__):
    
    with it('sum two fractions together') as test:
      expect(test.fraction + test.other_fraction).to.equal(Fraction(13,6))

    with it('sum a fraction with an int number') as test:
      expect(test.fraction + test.other_int).to.equal(Fraction(11,3))

    with it('sum an int number with a fraction') as test:
      expect(test.other_int + test.fraction).to.equal(Fraction(11,3))

  with context(Fraction.__cmp__):
    
    with context('when computing two fractions'):
      
      with it('return true when they have the same numerator and denominator') as test:
        expect(test.fraction == test.fraction_equal).to.be.true

      with it('return false when one of them do not have the same numerator or the same denominator') as test:
        expect(test.fraction == test.fraction_almost_equal).to.be.false

      with it('return true when one is greater than the other one') as test:
        expect(test.fraction > test.fraction_almost_equal).to.be.true

    with context('when computing a fraction with an int number'):
      
      with it('return true when the number is greater than the fraction') as test:
        expect(test.other_int > test.fraction).to.be.true

      with it('return true when the number is equal to the fraction') as test:
        expect(2 == Fraction(2)).to.be.true
  
  with context(Fraction.__sub__):
    
    with it('subtract a fraction from another one') as test:
      expect(test.fraction-test.other_fraction).to.equal(Fraction(-5,6))

    with it('subtract an int number from a fraction') as test:
      expect(test.fraction-test.other_int).to.equal(Fraction(-7,3))

    with it('subtract a fraction from an int number') as test:
      expect(test.other_int-test.fraction).to.equal(Fraction(7,3))

  with context(Fraction.__div__):
    
    with it('divides a fraction by another one') as test:
      expect(test.fraction/test.other_fraction).to.equal(Fraction(4,9))

    with it('divides a fraction by an int number') as test:
      expect(test.fraction/test.other_int).to.equal(Fraction(2,9))

    with it('divides an int number by a fraction') as test:
      expect(test.other_int/test.fraction).to.equal(Fraction(9,2))

  with context(Fraction.__invert__):
    with it('invert the numerator by the denominator') as test:
      expect(~test.fraction).to.equal(Fraction(test.fraction.denominator, test.fraction.numerator))

  with context(Fraction.__neg__):
    
    with it('negate the fraction numerator') as test:
      expect(-test.fraction).to.equal(Fraction(-test.fraction.numerator, test.fraction.denominator))
    
    with it('does not negate the fraction denominator') as test:
      expect(-test.fraction).not_to.equal(Fraction(-test.fraction.numerator, -test.fraction.denominator))