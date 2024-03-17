print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM FORMA triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo')
    