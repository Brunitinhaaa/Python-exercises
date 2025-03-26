import math

n = float(input('Enter a float number: '))

print(
'The square root of the number is: {:.2f}\n'
'The max round is {}\n'
'The min round is {}\n'
'The power is {:.4f}\n'
'The truncate is {}\n'
'The factorial is {:.0f}\n' 
.format(
    math.sqrt(n), 
    math.ceil(n), 
    math.floor(n), 
    math.pow(n,3), 
    math.trunc(n), 
    math.factorial(int(n))
    )
)

