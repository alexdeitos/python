def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situação de vários alunos;
       Criado por Alexsandro Deitos
    :param n: Uma ou mais notas do aluno.
    :param sit: Valor opcional para mostrar ou não a situação do aluno.
    :return: Dicionário contendo várias informações sobre a situação da turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5,2.5,9.5,sit=True)
print(resp)
help(notas)



