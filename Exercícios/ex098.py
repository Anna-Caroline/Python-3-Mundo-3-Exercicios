'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} e, {p}:')
    print('-='*20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end = ' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end = ' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1,10, 1)
contador(10,0, 2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem: ')
while True:
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))
    contador(inicio, fim, passo)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM')
