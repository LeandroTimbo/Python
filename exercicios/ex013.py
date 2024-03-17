salário = float(input('Qual é o salário do funcionário? RS'))
aumento = salário + (15 * salário / 100)
print('Um funcionário que ganhava RS{:.2f}, com 15% de aumento, passa a receber RS{:.2f}'.format(salário, aumento))
