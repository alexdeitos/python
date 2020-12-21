from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request, urlopen

qtd_papeis = int(input("Quantos papeis deseja analisar: "))
qtd = 0
while qtd < qtd_papeis:
    if qtd == 0:
        papel = input(f'Digite o código do papel a ser analisado: ')
    else:
        papel = input(f'\n\nDigite o código do proximo papel a ser analisado: ')
    # my_url = ('http://fundamentus.com.br/detalhes.php?papel=vale3', headers={'User-Agent': 'Mozilla/5.0'})
    # req = Request(f'http://fundamentus.com.br/detalhes.php?papel=vale3', headers={'User-Agent': 'Mozilla/5.0'})
    req = Request(f'http://fundamentus.com.br/detalhes.php?papel={papel}', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    urlopen(req).close()
    # abre a conexão e faz o download da página
    # uClient = uReq(my_url)
    # page_html = uClient.read()
    # fecha a conexão com a página
    # uClient.close()

    # configura amigavel a página
    page_soup = soup(webpage, "html.parser")

    # grabs each tag
    # pega o patrimonio liquido
    containers = page_soup.find_all("span", {"class": "txt"})
    # print(len(containers))
    i = 1
    for n in containers:
        # print(f'{i}',n)
        if i == 98:
            for v in n:
                ptr_liquido = v
        if i == 4:
            for v in n:
                cotacao_atual = v
        if i == 111:
            for v in n:
                luc_liquido = v
        if i == 28:
            for v in n:
                qtde_acoes = v
        i += 1
    print("----------------\n")
    print(f'{papel.upper()}:')
    print(f'Patrim. Liquido: ', ptr_liquido)
    print(f'Cotacao atual: ', cotacao_atual)
    print(f'Lucro Liquido: ', luc_liquido)
    print(f'Quantidade de Acoes: ', qtde_acoes)
    print("\n----------------\n")
    ptr_liquido = ptr_liquido.replace('.', '')
    cotacao_atual = cotacao_atual.replace(',', '.')
    luc_liquido = luc_liquido.replace('.', '')
    qtde_acoes = qtde_acoes.replace('.', '')

    # transforma em float as strings recebidas
    ptr_liquido = float(ptr_liquido)
    cotacao_atual = float(cotacao_atual)
    qtde_acoes = float(qtde_acoes)
    luc_liquido = float(luc_liquido)

    # Calculo do VPA
    # valor por ação - divide o valor do patrimonio liquido pela quantidade de acões disponíveis,
    # caso seja vendida esse é o valor recebido por ação
    vpa = ptr_liquido / qtde_acoes

    # Calculo de lucro por ação - lucro liquido da empresa dividido por ação será o que cada acionista recebera
    # caso a empresa entregue _todo seu lucro aos acionistas
    lpa = luc_liquido / qtde_acoes

    # P/L
    # O P/L
    # nada mais é do que o preço atual da ação, dividido pelo lucro por ação. Em outras palavras,
    # ele mostra quanto que os investidores estão dispostos a pagar por cada R$ 1 de lucro que a empresa tiver.
    pl = cotacao_atual / lpa

    # rpl quanto uma empresa gera de lucro sobre o seu próprio patrimonio em 12 meses
    rpl = luc_liquido / ptr_liquido
    # multiplica por 100 e teremos a % ao ano
    rpl = rpl * 100

    # dados de acordo com o retorno dos cálculos
    print()
    print(f'Valor por ação (VPA):{vpa:.2f}')
    print(f'Lucro por ação (LPA):{lpa:.2f}')
    print(f'O P/L da {papel} está em {pl:.2f}')
    print(f'Hoje {papel.upper()} gera lucro sobre o seu próprio patrimonio em 12 meses de: {rpl:.2f}%  ')
    qtd = qtd + 1
