nome = str(input('Qual é seu nome ? '))
if nome == 'Guilherme':
    print('Que nome bonito!')

elif nome =='Lucas' or nome == 'Maria':
        print('Seu nome é popular')

elif nome in 'Ana Jessica Julia':
    print('Belo nome feminino')

else:
    print('Seu nome é normal')
print('Tenhs um bom dia {}'.format(nome))