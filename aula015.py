'''cont = 1
while True:
    print(cont,'->', end=' ')
    cont += 1
    if cont >= 6:
        break
print('Acabou')'''

'''n  = 0
while n != 999:
    n = int(input('Digite um valor: '))'''

'''n  = s = 0
while n != 999:
    n = int(input('Digite um valor: '))
    s += n
s -= 999
print(s)'''

'''n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma de {s}')'''

nome = 'Jose'
idade = 20
salario = 500.35
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}') # PYTHON 3.6+
print('O {} tem {} anos'.format(nome, idade))# PYTHON 3
print('O %s tem %d anos' % (nome, idade))# PYTHON 2