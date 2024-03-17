peso = float(input('Qual e seu peso? (Kg) '))
altura = float(input('Qual e sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABEM, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce está em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce está em OBSIDADE!')
else:
    print('Voce está em OBSIDADE MORBIDA, cuidado!')
