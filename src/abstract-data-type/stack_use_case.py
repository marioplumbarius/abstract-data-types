from stack_implementation import Stack

# evaluate postfix

def run():
  s = Stack()
  expression = '12+3*'

  """ 
    there is no need to use parentheses to control the order of operations. to get the same result in infix, we would have to write:
        (1 + 2) * 3
  """

  for e in expression:
    if isOperand(e):
      e = int(e)
      s.push(e)
    else:
      result = do_operation(s, e)
      s.push(result)

  print s.items

def isOperand(n):
  try:
    int(n)
    return True
  except Exception, e:
    return False

def do_operation(stack, str_operator):
  result = 0
  while not stack.isEmpty():
    s = stack.pop()
    if str_operator == '+':
      result = result + s
    elif str_operator == '*':
      if result == 0: result = 1
      result = result * s

  return result

run()