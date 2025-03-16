d = float(input('Enter how many days you used the car: '))
km = float(input('Enter how many KM you drovethe car: '))

print('The total payable is: US$ {:.2f}' .format((d * 60) + (0.15 * km)))
