import re

def arithmetic_arranger(problems, result=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  arranged_problems = []
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  
  for prob in problems:
    p = prob.split()
    operand1, operator, operand2 = p[0], p[1], p[2]

    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits."

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(operand1), len(operand2)) + 2
    line1 += operand1.rjust(width)
    line2 += operator + operand2.rjust(width - 1)
    line3 += '-' * width
    sum = ''
    if operator == '+':
      sum = str(int(operand1) + int(operand2))
    else:
      sum = str(int(operand1) - int(operand2))
    line4 += sum.rjust(width)

    line1 += '    '
    line2 += '    '
    line3 += '    '
    line4 += '    '

  if result:
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip()
  else:
    arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() 

  return arranged_problems
