class Fraction:
  """
    rational numbers, expressed as a ratio of whole numbers, such as 5 / 6
    5 => numerator
    6 => denominator
  """

  def __init__(self, numerator, denominator=1):
    g = self.gcd(numerator, denominator)
    self.numerator = numerator / g
    self.denominator = denominator / g

  def __str__(self):
    return '%d/%d' % (self.numerator, self.denominator)

  def __mul__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator*other.numerator,
                    self.denominator*other.denominator)

  # enables multiplication even if the object is at the left/right in the evaluation expression
  # e.g.: 2*Fraction(3), Fraction(3)*2
  __rmul__ = __mul__

  def __add__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator * other.denominator + 
                    self.denominator * other.numerator,
                    self.denominator * other.denominator)

  # same as __rmul__
  __radd__ = __add__

  def __cmp__(self, other):
    diff = (self.numerator * other.denominator - 
      other.numerator * self.denominator)
    return diff

  def gcd(self, x, y):
    """
      Euclid's algorithm
      - If n divides m evenly, then n is the GCD. Otherwise the GCD is the GCD of n and the remainder of m divided by n.
    """
    if x % y == 0:
      return y
    else:
      return self.gcd(y, x%y)

  # TODO
  def __sub__(self, other):
    pass

  # TODO
  def __div__(self, other):
    pass

  # TODO
  def __neg__(self, other):
    pass

  # TODO
  def __invert__(self, other):
    pass

"""
  TODO
  - As an exercise, finish the implementation of the Fraction class so that it handles subtraction, division and exponentiation.
"""