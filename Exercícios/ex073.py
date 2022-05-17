''' Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atletico-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport-Recife',
         'EC Vitória', 'Coritiba','Avaí', 'Ponte Preta',
         'Atlético-GO')
print('=-' * 65)
print(f'Lista de times: {times}')
print('=-' * 65)
print(f'Os cinco primeiros são: {times[0:5]}')
print('=-' * 65)
print(f'Os quatro últimos são: {times[-4:]}')
print('=-' * 65)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 65)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
#for t in times:
    #print(t)
