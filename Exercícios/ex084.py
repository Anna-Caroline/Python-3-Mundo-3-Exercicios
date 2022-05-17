'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('='*30)
print(f'O dados foram {princ}')
print(f'A quantidade de pessoas cadastradas foi {len(princ)}')
print(f'O maior peso foi de {maior} quilos. peso de: ', end = ' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print(f'e o menor peso foi de {menor} quilos. Peso de: ', end = ' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')
