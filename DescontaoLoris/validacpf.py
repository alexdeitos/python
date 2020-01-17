def validaCpf(cpf, d1=0, d2=0, i=0):
    while i < 10:
        d1, d2, i = (d1 + (int(cpf[i]) * (11 - i - 1))) % 11 if i < 9 else d1, (
                d2 + (int(cpf[i]) * (11 - i))) % 11, i + 1
    return (int(cpf[9]) == (11 - d1 if d1 > 1 else 0)) and (int(cpf[10]) == (11 - d2 if d2 > 1 else 0))

cpf = '05007041980'
if not (validaCpf(cpf)):
    print('invalido')
else:
    print('ok cara')