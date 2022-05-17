'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.'''
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(lista): #varrendo toda a lista, pelo índice e pelo valor.
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa foi {lista}.')
print(f'A lista de valores pares foi {pares}.')
print(f'A lista de valores impares foi {impares}.')

