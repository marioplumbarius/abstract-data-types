from ivoire import describe, context
from expects import expect
from src.new_data_type.gcd import gcd

with describe(gcd) as it:
  with context('when x divides y evenly'):
    with it('y is the gdc') as test:
      expect(gcd(2,2)).to.equal(2)
  with context('when x does not divides y evenly'):
    with it('find the gdc of y and the reminder of x divided by y') as test:
      expect(gcd(9,4)).to.equal(gcd(4,9%4))