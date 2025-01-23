import math

print('arithmetic operators:')

n1 = int(input('Type first number:'))
n2 = int(input('Type second number:'))

print(f'Division: {n1 / n2}')
print(f'Multiplication: {n1 * n2}')
print(f'Sum: {n1 + n2}')
print(f'Subtraction: {n1 - n2}')
print(f'Power: {n1 ** n2} or {pow(n1, n2)}')
print(f'Integer Division: {n1 // n2}')
print(f'Rest of Division: {n1 % n2}')

print(f'Square Root:')
print(f'  {n1 ** (1/2)}')
print(f'  {math.sqrt(n1)}')
