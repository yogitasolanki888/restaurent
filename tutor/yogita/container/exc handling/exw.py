# class FormulaError(Exception):
#     pass
# def parse_input(user_input):
#     input_list = user_input.split()
#     print(input_list)
#     if len(input_list) != 3:
#        raise FormulaError('Input does not consist of three elements')
#     n1, op, n2 = input_list
#     try:
#            n1 = int(n1)
#            n2 = int(n2)
#     except ValueError:
#            raise FormulaError('The first and third input value must be numbers')
#     return n1, op, n2


# def calculate(n1, op, n2):

#   if op == '+':
#     return n1 + n2
#   if op == '-':
#     return n1 - n2
#   if op == '*':
#     return n1 * n2
#   if op == '/':
#     return n1 / n2
#   raise FormulaError('{0} is not a valid operator'.format(op))


# while True:
#   user_input = input('enter  number ')
#   if user_input == 'quit':
#     break
#   n1, op, n2 = parse_input(user_input)
#   result = calculate(n1, op, n2)
#   print(result)


# x=0
# if x == 0:
#     print(x is 1)

def callover(i):
    print(10/i)
# callover(0)


try:
    i = callover('x')
except ZeroDivisionError as e:
    print('Cannot divide by zero')
except TypeError as e:
    print('Expecting a non-zero number')
else:
    print('No exception occurred')
finally:
    print('This is always executed')


