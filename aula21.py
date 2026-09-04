#INTERACTIVE HELP
''' help()

exemplo :

help(print)
    len - print - input - datatime - exit - quit

OU OUTRO JEITO

print(input.__docs__)'''


#DOCSTRINGS

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
     Função criada por Gustavo Guanabara
     Canal Curso em video
     Data da aula 17/07/2026
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print()

contador(2, 10, 2)
contador(0,100,10)

help(contador)'''

#PARAMENTROS OPCIONAIS

'''def somar(a=0, b=0, c=0):
    """
    ->Faz a soma de tres valores e mostra o resultado na tela
    :param a: o primeiro valor
    :param b:o segundo valor
    :param c: o terceiro valor
     Função criada por Gustavo Guanabara
     Canal Curso em video
     Data da aula 17/07/2026
     """
    s = a + b + c
    print(f'A soma vale {s}',end='')
    print()

somar(3,2)
somar(b=4,c=2)'''


#ESCOPO VARIAVEIS


'''def teste():
    x = 0 #Variavel local existe apenas aqui dentro da função 
    print(f'Na função teste,n vale {n}')
    print(f'Na função teste,x vale {x}')


#Programa principal
n=2 #Variavel global
print(f'NO programa principal,n vale {n}')
teste()
print(f'No programa principal,n vale {x}')


def funcao():
    n1 = 4
    print(f'O valor N1 DENTRO VALE {n1}')

n1 = 2
funcao()
print(f'O valor N1 FORA VALE {n1}')'''


#RETORNANDO VALORES


'''def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(3,2,5)
soma(2,2)
soma(6)'''


'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3,2,5)
r2 = soma(2,2)
r3 = soma(6)

print(f'Os resultados foram {r1},{r2} e {r3}')'''


'''def factorial(num=1):
     f = 1
     for c in range(num,0,-1):
         f*= c
     return f

n = int(input('Digite um numero:'))
print(f'O factorial de {n} é igual a {factorial(n)}')
f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Os resultados são {f1}, {f2} e  {f3}')'''


def par(n=0):
    if num % 2 == 0:
        return True
    else:
          return False

num = int(input('Digite um numero:'))
if par(num):
    print('È par!')
else:
    print('Nâo é par!')
print(par(num))