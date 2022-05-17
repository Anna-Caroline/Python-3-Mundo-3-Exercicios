'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0: #sinal de que não está vazio
            pilha.pop() # remove o último elemento
        else:
            pilha.append(')') #sinal de que teve mais parentese fechando que abrindo
            break
if len(pilha) == 0: #cada parentese que abriu teve a sua relaçãp com parentese fechando
    print('Sua expressão está válida.')
else: # Se o len da pilha foi acima de zero
    print('Sua expressão está errada.')


