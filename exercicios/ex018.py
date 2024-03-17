from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja'))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('o ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
print('o ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))
 