#nome=input("Qual o seu nome?")
#print('Prazer em te conhecer{:=20}!'.format(nome))
#print('Prazer em te conhecer{:<20}!'.format(nome))
#print('Prazer em te conhecer{:>20}!'.format(nome))
#print('Prazer em te conhecer{:^20}!'.format(nome))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 =int(input('Um valor: '))
n2=int(input('Outro valor: '))
a=n1+n2
sb=n1-n2
m=n1*n2
d=n1/n2
p=n1**n2
di=n1//n2
r=n1%n2
print('\n A Soma {} ,\n A Mubtração {} ,\n A Multiplicação {} ,\n A Divisão {} '.format(a,sb,m,d),end=' ')
print('Agora a Potencia {} , Divisão inteira {}, Resto da Divisão {}'.format(p,di,r))
