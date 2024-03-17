from random import randint
from time import sleep
computador = randint(0, 5) #progama que faz o computador "PENSAR"
print('-=' * 26)
print('vou pensar em número entre 0 e 5. tente adivinhar...')
print('-=' * 26)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABEM! você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
    