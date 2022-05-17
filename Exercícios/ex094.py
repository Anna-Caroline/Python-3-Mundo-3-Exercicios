''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = dict()
galera = list()
soma = med = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F: ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas sim ou não.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo tempos {len(galera)} cadastradas.')
med = soma/len(galera)
print(f'A média de idades é {med:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end = '')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end = ' ')
print()
print('Lista das pessoas que estão acima da média da idade: ', end=' ')
for p in galera:
    if p['idade'] >= med:
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<<<ENCERRADO>>>>>>')









