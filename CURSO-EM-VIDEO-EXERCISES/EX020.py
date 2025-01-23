import random

ni = int(input('A random number will be generated from a range, enter the start of the range: '))
nf = int(input('now, enter the end of the range: '))

print('The next number is random: {}' .format(random.randint(ni, nf)))
