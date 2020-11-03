f = 'Curso em Vídeo Python'
f = f.strip() #Tira os espaços inúteis no começo e no final da string

print(f[3:]) #Digita a string a partir do 3º caractere

print(f[3::2]) #Digita a partir do terceiro e pulando de 2 em 2 caractere

print(f.upper()) #Todas as letras Maiúsculas

print(f.lower()) #Todas as letras Minúsculas

print(f)
print(f.capitalize()) #A frase digitada começará com letra maiúscula

print(f.title()) #Todas as palavras começam com letra maiúscula

list = f.split() #Cria uma lista com as palavras separadamente

print(list)
print('-'.join(list)) #Adiciona algo nos espaços da lista

#print em mais de uma linha é só colocar """ (três áspas no começo e no final

print(len(f.strip())) #Mostra o número de caracteres

print(f.replace('Curso', 'Aula')) #Troca uma palavra da string

print('Curso' in f) #Verifica se existe tal palavra na string

print(f.find('Vídeo')) #Encontra e diz a posição da palavra na string

print(f.lower().find('python')) #Aqui eu deixei todos os carácteres em
# minúsculo para encontrar uma frase que poderia estar com alguma letra em
# maiúsculo
print(list[2]) #Mostra determinado item da lista (começando por 0)

print(list[2] [3]) #Mostra a letra de determinado item (nesse caso, na 2º
# palavra, 3º caractere, começando por 0)

# tupla.index('Palavra') é o .find da tupla

