'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as
funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando..'''
def aumentar(preço = 0, taxa = 0, formato=False):
    '''
    Calcula o aumento e decaimento de um preço
    :param preço: recebe o preço
    :param taxa: a taxa a ser acrescida no preço
    :param formato: formata o preço para R$
    :return: retorna o valor
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res)


def dobro(preço = 0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: {diminuir(preço, taxar, True)}')
    print('-' * 30)

