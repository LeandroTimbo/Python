sexo = str(input('Informe Seu Sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso'.format(sexo))