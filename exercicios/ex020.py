from random import shuffle
n1 = input('primeiro aluno:')
n2 = input('segudo aluno')
n3 = input('teceiro aluno')
n4 = input('quarto aluno')
lista = [n1, n2, n3, n4]
sor = shuffle(lista)
print('a ordem de apresentação sera')
print(lista)