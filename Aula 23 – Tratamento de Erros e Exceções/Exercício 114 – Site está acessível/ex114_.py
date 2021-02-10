"""Crie um código em python que teste se o site Pudim está acessível pelo computador usado."""
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('deu erro!')
else:
    print('tudo ok')
