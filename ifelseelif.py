a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0:
    print('Numero par digitado')
else:
    print('Nenhum numero par foi digitado')  