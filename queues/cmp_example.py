class Golfer():
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def __str__(self):
    return '%-16s: %d' % (self.name, self.score)

  def __cmp__(self, other):
    if self.score < other.score: return 1
    if self.score > other.score: return -1
    return 0