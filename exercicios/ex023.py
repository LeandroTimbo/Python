num = int(input('Informe um Número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('unidadede: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(um))