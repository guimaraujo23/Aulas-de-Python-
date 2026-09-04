print('\033[1;31;43m Ola, mundo!')
print('\033[4;30;45m Ola, mundo!\033[m')
print('\033[30m Ola, mundo!\033[m')
print('\033[7;30m Ola, mundo!\033[m')
print('\033[37m Ola, mundo!\033[m')
print('\033[0;33;44m Ola, mundo!\033[m')
print('\033[7;33;44m Ola, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a,b))

nome = 'Guilherme'
print('Olá! Muito prazer em te conhecer!{}{}{} !!!'.format('\033[4;34m',nome,'\033[m'))

nome = 'Guilherme'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m',}

print('Ola! Muito Prazer em te conhecer!{}{}{} !!!'.format(cores['pretobranco'],nome,cores['limpa']
                    ,nome))
