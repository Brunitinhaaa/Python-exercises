from math import ceil

width = float(input('enter the width of you wall: '))
height = float(input('enter the height of your wall: '))

print('Your wall is {:.2f} square meters, and you can paint your inteire wall with {} gallons of wall paint' .format((width * height),ceil(((width * height)/2))))
