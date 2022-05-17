'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito'
        'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis'
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'você digitou o {cont[num]}.')
    else:
        print('Você não digitou um número entre 0 e 20.')
    nome = ' '
    while nome not in 'SsNn':
        nome = str(input('Deseja continuar? ')).strip().upper()[0]
    if nome == 'N':
         break
    else:
        print('Tente novamente')
prin('Fim.')

