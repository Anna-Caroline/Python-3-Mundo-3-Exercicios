'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'A média do aluno {aluno["nome"]} é: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7 :
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
