'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'{k} : {v}')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'Na partida {i} ele fez {v} gols.')
print(f'O total de gols foi {jogador["Total"]}')





