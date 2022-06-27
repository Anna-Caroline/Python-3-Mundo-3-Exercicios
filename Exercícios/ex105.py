'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''
def notas(*n, sit=False):
    '''
    ---> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas (aceita várias)
    :param sit: opcional. Indica a situação do aluno a partir da média
    :return: dicionário contendo as informações
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa!'
        elif 5 <= r['média'] < 7:
            r['situação'] = 'Razoável.'
        else:
            r['situação'] = 'Ruim!'
    return r


#Programa Principal
resp = notas(4.5, 6.7, 8, 9, sit=True)
print(resp)
# help(notas)