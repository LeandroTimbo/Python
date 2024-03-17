casa = float(input('Qual o valor da casa: R$ '))
salário = float(input('Salario da comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para comprar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end = ' ')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONSEDIDO!')
else:
    print('Empréstimo NEGADO!')
