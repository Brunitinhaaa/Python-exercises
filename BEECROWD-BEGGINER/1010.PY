'''
beecrowd | 1010
Simple Calculate
Adapted by Neilor Tonin, URI  Brazil

Timelimit: 1
In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

Input Samples	Output Samples
12 1 5.30
16 2 5.10

VALOR A PAGAR: R$ 15.50

13 2 15.30
161 4 5.20

VALOR A PAGAR: R$ 51.40

1 1 15.10
2 1 15.10

VALOR A PAGAR: R$ 30.20
'''

P1_cod, P1_qnt, P1_pric = input().split()
P1_qnt = int(P1_qnt)
P1_pric = float(P1_pric)

P2_cod, P2_qnt, P2_pric = input().split()
P2_qnt = int(P2_qnt)
P2_pric = float(P2_pric)

print('VALOR A PAGAR: R$ {:.2f}'.format((P1_pric*P1_qnt)+(P2_pric*P2_qnt)))

