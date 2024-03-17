nome = str(input('Digite seu nome completo: ')).strip()
dividir = nome.split()
print('Seu primeiro nome e {}'.format(dividir[0]))
print('Seu segundo nome e {}'.format(dividir[len(dividir)-1]))
