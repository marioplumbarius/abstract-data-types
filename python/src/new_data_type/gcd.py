def gcd(x, y):
  """
    Euclid's algorithm
    - If n divides m evenly, then n is the GCD. Otherwise the GCD is the GCD of n and the remainder of m divided by n.
  """

  if x % y == 0:
    return y
  else:
    return gcd(y, x%y)