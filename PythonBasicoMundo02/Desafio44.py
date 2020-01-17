"""

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros

"""
print(("=="*8)+ " LOJAS UNIFICAS "+("=="*8))
valor = float(input("Digite o valor das compras R$?"))
print("""QUAL A FORMA DE PAGAMENTO:
   [ 1 ] . Á VISTA DINHEIRO/CHEQUE
   [ 2 ] . Á VISTA CARTÃO 
   [ 3 ] . 2X CARTÃO
   [ 4 ] . 3X OU MAIS NO CARTÃO
""")
condicao = "invalida"
while condicao == "invalida":
    forma_pagamento = int(input("==>> "))
    if forma_pagamento == 1:
        pagar = valor - (valor * 10 /100)
        condicao = "Á VISTA DINHEIRO/CHEQUE"
    elif forma_pagamento == 2:
        pagar = valor - (valor * 5 / 100)
        condicao = "Á VISTA CARTÃO"
    elif forma_pagamento == 3:
        pagar = valor
        condicao = "2X CARTÃO"
    elif forma_pagamento == 4:
        qtd_parcelas = int(input("Quantas parcelas?\n==>"))
        pagar = (valor + (valor * 20 / 100)) / qtd_parcelas
        if qtd_parcelas == 3:
            condicao = "3 X NO CARTÃO"
        else:
            condicao = "{} X NO CARTÃO".format(qtd_parcelas)
    else:
        print("Opção Inválida")
        continue
print("=" *50 + "COMPRA FINALZADA" +  "="*50+"\n")
print("A condição de pagamento escolhida foi {} e o valor da compra ficou R${:.2f}".format(condicao,pagar))
