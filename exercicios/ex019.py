from random import choice
al1 = input('qual nome do primeiro aluno:')
al2 = input('o nome do segundo aluno:')
al3 = input('o terceiro:')
al4 = input('e quarto:')
lista = [al1, al2, al3, al4]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))