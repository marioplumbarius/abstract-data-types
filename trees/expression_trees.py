from tree import Tree
from printing_trees import printTreePostorder

def parse_string_to_token_list(string):
  """ parses a string and convert it to a token list """
  str_clone = string[:]
  str_list = list(str_clone)
  str_list.append('end')
  str_list_len = len(str_list)
  
  for i in range(str_list_len):
    str_list[i] = convert_to_int(str_list[i])
  return str_list

def convert_to_int(str_int):
  """ converts a string int to int """
  try:
    str_int = int(str_int)
  except Exception, e:
    pass
  return str_int


def getToken(tokenList, expected):
  """ removes the expected token from the token list """
  if tokenList[0] == expected:
    del tokenList[0]
    return True
  else:
    return False

def stripParenthesis(tokenList):
  """ remove and return the next number from a token list """
  if getToken(tokenList, '('): 
    x = getSum(tokenList)
    if not getToken(tokenList, ')'):
      raise ValueError, 'missing parenthesis'
    return x
  else:
    x = tokenList[0]
    if not isinstance(x, int): return None
    tokenList[0:1] = []
    return Tree(x, None, None)

def getProduct(tokenList):
  """ generates an expression tree for products """
  a = stripParenthesis(tokenList)
  if getToken(tokenList, '*'):
    b = getProduct(tokenList)
    return Tree('*', a, b)
  else:
    return a

def getSum(tokenList):
  a = getProduct(tokenList)
  if getToken(tokenList, '+'):
    b = getSum(tokenList)
    return Tree('+', a, b)
  else:
    return a

def compute(tokenList):
  tokenList = parse_string_to_token_list(tokenList)
  return getSum(tokenList)