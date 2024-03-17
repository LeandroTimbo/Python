alu = int(input('quantos dias alugado?'))
km = float(input('quantos Km rodados?'))
pago = (alu * 60) + (km * 0.15)
print('O total a pagar é de RS{:.2f}'.format(pago))
