n1 = int(input('type first number: '))
n2 = int(input('type second number: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di =  n1 // n2
rd = n1 % n2

print('The some is {}, the product is {}, the division is {:.3f}, the integer division is {}, the remainder of the division is {}' . format(s, m, d, di, rd))

print('Type of s:', type(s))
print('Type of m:', type(m))
print('Type of d:', type(d))
print('Type of di:', type(di))
print('Type of rd:', type(rd))

print('or:')

variables = {'s': s, 'm': m, 'd': d, 'di': di, 'rd': rd}

for name, value in variables.items():
    print(f'Type of {name}: {type(value)}')
