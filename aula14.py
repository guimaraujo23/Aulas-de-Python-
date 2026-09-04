'''for c in range(1,10):
    print(c)
print('fim')'''

'''for c in range(1,3):
    n = int(input('Digite um valor: '))
print('fim')'''


'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''


'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('fim')'''


'''r ='S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n !=0:
      if n % 2 == 0:
        par += 1
      else:
        impar += 1
soma = par + impar
print('Você digitou {} valores PARES e {} valores IMPARES ao todo tem {} NUMEROS'.format(par, impar,soma))