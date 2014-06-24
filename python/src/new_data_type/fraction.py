from gcd import gcd

class Fraction:
  """ implementation of a fraction  using built-in python methods """

  def __init__(self, numerator, denominator=1):
    """ create a fraction from a numerator and denominator """
    g = gcd(numerator, denominator)
    self.numerator = numerator / g
    self.denominator = denominator / g

  # TODO: how come will I be tested?
  def __str__(self):
    """ representation of the fraction: numerator / denominator """
    return '%d/%d' % (self.numerator, self.denominator)

  def __mul__(self, other):
    """ implement fraction multiplication """
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator*other.numerator,
                    self.denominator*other.denominator)

  __rmul__ = __mul__

  def __add__(self, other):
    """ implement fraction adding """
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator * other.denominator + 
                    self.denominator * other.numerator,
                    self.denominator * other.denominator)

  __radd__ = __add__

  def __cmp__(self, other):
    """ implement fraction comparisson """
    if isinstance(other, int):
      other = Fraction(other)
    diff = (self.numerator * other.denominator - 
      other.numerator * self.denominator)
    return diff

  def __sub__(self, other):
    """ implement fraction subtraction """
    return -other+self

  def __rsub__(self, other):
    return -self+other

  def __div__(self, other):
    """ implement fraction division """
    if isinstance(other, int):
      other = Fraction(other)
    return self*~other

  def __rdiv__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return ~self*other

  def __neg__(self):
    """ implement fraction negation """
    return Fraction(-self.numerator, self.denominator)

  def __invert__(self):
    """ implement fraction inversion """
    return Fraction(self.denominator, self.numerator)