import random

n1 = input('Enter the name of the firs student: ')
n2 = input('Enter the name of the second student: ')
n3 = input('Enter the name of the third student: ')
n4 = input('Enter the name of the fourth student: ')

names = [n1, n2, n3, n4]

random.shuffle(names)

print('The order of students who must present their work is: {}' .format(names))