''' Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas sim ou não.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end = ' ')
print()
print('--'*30)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('--'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! O jogador {busca} não existe.')
    else:
        print(f'----- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('--' * 30)
print('<< VOLTE SEMPRE >>')



