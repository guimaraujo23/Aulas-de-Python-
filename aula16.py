print('Ex01')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche)
print('-='*15)


print('Ex02')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[1])
print('-='*15)


print('Ex03')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[3])
print('-='*15)


print('Ex04')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[-2])
print('-='*15)


print('Ex05')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[1:3])
print('-='*15)


print('Ex06')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[2:])
print('-='*15)


print('Ex07')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[:2])
print('-='*15)


print('Ex08')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(lanche[-3:])
print('-='*15)


print('Ex09')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
#Tuplias são imutaveis
#lanche[1]='Refrigerante'
print(lanche[1])
print('-='*15)


print('Ex10')
lanche = 'Hamburguer','Suco','Pizza','Pudim','Batata Frita'
print(len(lanche))
print('Comi pra caramba!!!')
print('-='*15)


print('Ex11')
lanche = 'Hamburguer','Suco','Pizza','Pudim'

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-='*15)


print('Ex12')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-='*15)


print('Ex13')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-='*15)



print('Ex14')
lanche = 'Hamburguer','Suco','Pizza','Pudim'
print(sorted(lanche))#sorted ordem alfabertica
print(lanche)
print('-='*15)

print('Ex15')
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print('-='*15)

print('Ex16')
a = (2,5,4)
b = (5,8,1,2)
c =  b + a
print(c)
print('-='*15)


print('Ex17')
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(len(c))
print('-='*15)


print('Ex18')
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c.count(5))


print('Ex19')
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(c.index(8))
print('-='*15)


print('Ex20')
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(c.index(5,1))
print('-='*15)

print('Ex21')
pessoa = ('Gustavo',39,'M',99.98)
print(pessoa)
print('-='*15)


print('Ex22')
pessoa = ('Gustavo',39,'M',99.98)
del pessoa
print(pessoa)






