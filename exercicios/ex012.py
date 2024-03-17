preço = float(input('qual o valor do produto? RS'))
p1 = preço-(preço * 5 / 100)
print('o produto que custava RS{:.2f}, na promoção de 5% vai custar {:.2f}'.format(preço, p1))
