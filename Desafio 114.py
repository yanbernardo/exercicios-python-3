import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')
except:
    print('\033[1;31mO site do Pudim não está acessível no momento...\033[m')
else:
    print('\033[1;32mO site do Pudim está acessível no momento!\033[m')