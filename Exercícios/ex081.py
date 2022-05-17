'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista =[]
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente {lista}')
if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

