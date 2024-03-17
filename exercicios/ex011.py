l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
área = l * a
print('Sua parede tem a dimensão de {}x{} e sua área e de {}m².'.format(l, a, área))
tinta = área / 2
print('para pintar essa parede, você precisará de {}l de tinta'.format(tinta))