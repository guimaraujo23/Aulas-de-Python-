try:
   a = int(input('Digite um numero: '))
   b = int(input('Digite outro numero: '))
   r = a / b
except Exception as erro:
    print(f'Problema com o erro: {erro.__cause__}')
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dados que você digitou:')
except ZeroDivisionError:
    print('Nâo é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nâo informar os dados ')

else:
   print(f'O numero digitado foi {r:.1f}')
finally:
    print('Volte sempre!')