teste = list()
teste.append('Guilherme')
teste.append(23)
galera = list()
#galera.append(teste)
galera.append(teste[:])
teste[0]='Maria'
teste[1]= 22
galera.append(teste[:])
print(galera)


galera=[['Joâo',19],['Ana',33],['Joaquim',16],['Maria',45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(p)
print('-' * 40)
for p in galera:
    print(p[0])
print('-' * 40)
for p in galera:
    print(p[1])
print('-' * 40)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
print('-' * 40)


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('A sua idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print('-' * 40)
print(f'Temos {totmai} maiores,e {totmen} menores de idade')