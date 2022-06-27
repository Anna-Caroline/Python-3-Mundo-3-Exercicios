'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site foi acessado com sucesso!')
    print(site.read()) #consegue acessar o código do site
