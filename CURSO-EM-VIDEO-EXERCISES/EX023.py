import math

a = float(input('Enter the angle: '))

print(
    'The value of sine: {:.2f} \n'
    'cosine: {:.2f} \n'
    'tangent: {:.2f}' 
    .format
    (math.sin(math.radians(a)),
      math.cos(math.radians(a)), math.tan(math.radians(a))))

