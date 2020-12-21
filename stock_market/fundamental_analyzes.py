papel = str(input('Papel a ser analisado: '))
cotacao_atual = input("valor atual da cotaçao: ").replace(',','.')
ptr_liquido = input(f'patrimonio liquido da empresa: ').replace('.','')
luc_liquido = input(f'Qual o lucro liquido do {papel} nos últimos 12 meses:').replace('.','')
qtde_acoes = input('quantidade total de ações da empresa no mercado: ').replace('.','')

#transforma em float as strings recebidas
ptr_liquido = float(ptr_liquido)
cotacao_atual = float(cotacao_atual)
qtde_acoes = float(qtde_acoes)
luc_liquido = float(luc_liquido)

# Calculo do VPA
#valor por ação - divide o valor do patrimonio liquido pela quantidade de acões disponíveis,
# caso seja vendida esse é o valor recebido por ação
vpa = ptr_liquido / qtde_acoes

#Calculo de lucro por ação - lucro liquido da empresa dividido por ação será o que cada acionista recebera
# caso a empresa entregue _todo seu lucro aos acionistas
lpa = luc_liquido / qtde_acoes

# P/L
#O P/L
# nada mais é do que o preço atual da ação, dividido pelo lucro por ação. Em outras palavras,
# ele mostra quanto que os investidores estão dispostos a pagar por cada R$ 1 de lucro que a empresa tiver.
pl = cotacao_atual/lpa


#rpl quanto uma empresa gera de lucro sobre o seu próprio patrimonio em 12 meses
rpl =  luc_liquido / ptr_liquido
# multiplica por 100 e teremos a % ao ano
rpl = rpl * 100

# dados de acordo com o retorno dos cálculos
print(f'Valor por ação (VPA):{vpa:.2f}')
print(f'Lucro por ação (LPA):{lpa:.2f}')
print(f'O P/L da {papel} está em {pl:.2f}')
print(f'Hoje {papel} gera lucro sobre o seu próprio patrimonio em 12 meses de: {rpl:.2f}%  ')

