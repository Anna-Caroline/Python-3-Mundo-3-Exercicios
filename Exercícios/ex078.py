''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista = []
maior = menor = 0
for v in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print(f'A lista criada foi : {lista} o maior valor foi {maior} nas posições: ', end = '')
for i, c in enumerate(lista):
    if c == maior:
        print(f'{i}...')
print(f'E o menor valor foi {menor} nas posições: ')
for i, c in enumerate(lista):
    if c == menor:
        print(f'{i}...')

