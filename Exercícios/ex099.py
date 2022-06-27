''' Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* num):
    cont = mai = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end = ' ')
        sleep(0.5)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.\nE o maior valor informado foi {mai}.')



maior(2, 8, 4, 8, 9, 1, 3)
maior(2,3,6,1)
maior()
maior(4,6)