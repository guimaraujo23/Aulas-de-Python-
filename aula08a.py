#import math
from math import sqrt,floor,ceil
n1=int(input('Digite um valor: '))
raiz=sqrt(n1)
#raiz= math.sqrt(n1)
#print('A raiz do numero {} e equivalente a {}'.format(n1,math.floor(raiz)))
#print('A raiz do numero {} e equivalente a {}'.format(n1, math.ceil(raiz)))
#rint('A raiz do numero {} e equivalente a {:.2f}'.format(n1,math.raiz))

print('A raiz do numero {} e equivalente a {}'.format(n1,floor(raiz)))
print('A raiz do numero {} e equivalente a {}'.format(n1, ceil(raiz)))
print('A raiz do numero {} e equivalente a {:.2f}'.format(n1,raiz))