pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 18}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
pessoas['nome']='Guilherme'
pessoas['peso']= 98.5
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k}: {v}')
print('-' * 30)
brasil = list()
estado1 = {'uf':'Rio de janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-' * 30)

estado = dict()
brasil = list()
for c in range(0, 3):
     estado['uf'] = str(input('Unidade Federativa: '))
     estado['sigla'] = str(input('Sigla do Estado: '))
     brasil.append(estado.copy())
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k}tem valor {v}')
for e in brasil:
    for v in e.items():
        print(v, end='  ')
    print()



