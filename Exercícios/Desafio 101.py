def voto(nasc):
    from datetime import datetime
    idade = datetime.today().year - nasc
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos o voto é NEGADO'


# Programa Principal
ano = int(input('Ano de Nascimento: '))
print(voto(ano))
