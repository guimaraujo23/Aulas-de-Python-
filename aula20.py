from signal import valid_signals

print('-'*30)
print(' CURSO EM VIDEO')
print('-'*30)
print('-'*30)
print(' APRENDA PYTHON')
print('-'*30)
print('-'*30)
print('GUSTAVO GUANABARA')
print('-'*30)


def lin():
    print('-'*30)

#Programa Principal
lin()
print(' CURSO EM VIDEO')
lin()
print(' APRENDA PYTHON')
lin()
print('GUSTAVO GUANABARA')
lin()

def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

#Programa Principal
titulo(' CURSO EM VIDEO')
titulo(' APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')



def mensagem(msg):
    print('-'*30)
    print(f' {msg} ')
    print('-'*30)

mensagem('SISTEMA DE ALUNOS')

'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)'''

def soma(a, b):
   print(f'A = {a} e B = {b} ')
   s = a + b
   print(f'A soma A + B = {s} ')
   print('-='*30)


soma(4,5)
soma(8,9)
soma(2,1)
soma(b=4,a=5)



def contador(* num):
     for valor in num:
        print(valor, end=' ')
     print('Fim')

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)
print('-'*30)
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print('-'*30)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)




def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')


soma(5,2)
soma(2,9,4)
