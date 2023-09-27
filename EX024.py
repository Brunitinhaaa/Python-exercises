import random

n1 = input('Enter the name of the firs student: ')
n2 = input('Enter the name of the second student: ')
n3 = input('Enter the name of the third student: ')
n4 = input('Enter the name of the fourth student: ')

names = [n1, n2, n3, n4]

print('-' * 50)
print('The student who will clean the blackboard is: {}' .format(random.choice(names)))
