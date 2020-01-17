def voto(idade):
    from datetime import date
    i = date.today().year - idade
    if i < 16:
        print(f'Com {i} anos: VOTO NEGADO!')
    elif 16 <= i < 18 or i > 65:
        print(f'Com {i} anos: VOTO É OPCIONAL!')
    else:
        print(f'Com {i} anos: VOTO É OBRIGATÓRIO!')


voto(idade=int(input('Ano de nascimento: ')))