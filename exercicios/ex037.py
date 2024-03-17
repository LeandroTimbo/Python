num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converção:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é ingual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é ingual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é ingual a {}'.format(num, hex(num)[2:]))
else:
    print('opção e inválida. tente novamente.')
