from gcd import gcd

class Fraction:
  """
    rational numbers, expressed as a ratio of whole numbers, such as 5 / 6
    5 => numerator
    6 => denominator
  """

  def __init__(self, numerator, denominator=1):
    g = gcd(numerator, denominator)
    self.numerator = numerator / g
    self.denominator = denominator / g

  # TODO: how come will I be tested?
  def __str__(self):
    return '%d/%d' % (self.numerator, self.denominator)

  def __mul__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator*other.numerator,
                    self.denominator*other.denominator)

  __rmul__ = __mul__

  def __add__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return Fraction(self.numerator * other.denominator + 
                    self.denominator * other.numerator,
                    self.denominator * other.denominator)

  __radd__ = __add__

  def __cmp__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    diff = (self.numerator * other.denominator - 
      other.numerator * self.denominator)
    return diff

  def __sub__(self, other):
    return -other+self

  def __rsub__(self, other):
    return -self+other

  def __div__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return self*~other

  def __rdiv__(self, other):
    if isinstance(other, int):
      other = Fraction(other)
    return ~self*other

  def __neg__(self):
    return Fraction(-self.numerator, self.denominator)

  def __invert__(self):
    return Fraction(self.denominator, self.numerator)