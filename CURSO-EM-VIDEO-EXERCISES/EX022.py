import math

n1 = float(input('Enter the opposite side of the triangle: '))
n2 = float(input('now, insert the adjacent side of the triangle: '))

print('The value of the hypotenuse is {:.2f}' 
      .format(math.sqrt(math.pow(n1,2) 
               + math.pow(n2,2))))

print('The value of the hypotenuse is {:.2f}' 
      .format(math.hypot(n1,n2)))