def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario Preferio não digitar esse numero.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuario preferio não digitar esse numero.\033[m')
            return 0
        else:
            return n
            

# Progama principal
n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
