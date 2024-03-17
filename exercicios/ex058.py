from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acadei de pensar em um número entre 0 a 10.')
print('Sera que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual e seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acadou com {} tentativa. parabéns!'.format(palpite))
    