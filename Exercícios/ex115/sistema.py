from lib.interface import *
from time import sleep
from lib.arquivo import *
# o * importa tudo

arqui = 'CursoEmVideo.txt'
if not arquivoExiste(arqui):
    criarArquivo(arqui)

while True:
    resposta = menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoaa', 'Sair do sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arqui)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arqui, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

