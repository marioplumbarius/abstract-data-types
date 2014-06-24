from fraction import Fraction

""" adding """
print Fraction(2,3) + Fraction(3,2) # 13/6
print Fraction(2,3) + 3 # 11/3
print 3 + Fraction(2,3) # 11/3

""" multiplication """
print Fraction(2,3) * Fraction(3,2) # 1/1
print Fraction(2,3) * 3 # 2/1
print 3 * Fraction(2,3) # 2/1

""" subtraction """
print Fraction(2,3) - Fraction(3,2) # -5/6
print Fraction(2,3) - 3 # -7/3
print 3 - Fraction(2,3) # 7/3

""" division """
print Fraction(2,3) / Fraction(3,2) # 4/9
print Fraction(2,3) / 3 # 2/9
print 3 / Fraction(2,3) # 9/2