'''
beecrowd | 1003
Simple Sum
Adapted by Neilor Tonin, URI  Brazil

Timelimit: 1
Read two integer values, in this case, the variables A and B. After this, calculate the sum between them and assign it to the variable SOMA. Write the value of this variable.

Input
The input file contains 2 integer numbers.

Output
Print the message "SOMA" with all the capital letters, with a blank space before and after the equal signal followed by the corresponding value to the sum of A and B. Like all the problems, don't forget to print the end of line, otherwise you will receive "Presentation Error"

Input Samples	
30, 10
-30, 10
0, 0

Output Samples

SOMA = - 40
SOMA = -20
SOMA = 0
'''

A = int(input())
B = int(input())

print('SOMA = {}'.format(A+B))