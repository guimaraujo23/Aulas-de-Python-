'''nome = str(input('Qual é um nome: '))
n = nome.lower()
if n == 'guilherme':
   print('Que nome lindo você tem! ')
else:
    print('Que nome tão normal!')
print('Bom dia {}'.format(n))'''


n1 =float(input('Digite um numero: '))
n2=float(input('Digite a nota da 2 prova: '))
m = (n1+n2)/2
if m >= 6.0:
     print('Parabens você passou com uma media de {}!'.format(m))

else:
    print('Infelizmente sua media foi de {} e você não passou!'.format(m))
    print('--ESTUDE MAIS--')