nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome…')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('seu nome em minúscula é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split(' ')
print('seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))