t = float(input('type a temperature in fahrenheit: '))

print('This temperature {} in Fahrenheit corresponds {:.2f} in Celsius!' .format(t,((t - 32)/1.8)))

t = float(input('type a temperature in Celsius: '))

print('This temperature {} in Celsius corresponds {:.2f} in Fahrenheit!' .format(t,((t * 1.8)+32)))