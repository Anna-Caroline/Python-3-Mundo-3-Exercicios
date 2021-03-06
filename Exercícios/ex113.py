'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue #Joga pra dentro do While de novo, vai ficar dando erro
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue #Joga pra dentro do While de novo, vai ficar dando erro
        except(KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')
