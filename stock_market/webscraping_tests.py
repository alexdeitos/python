from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


qtd_papeis = int(input("Quantos papeis deseja analisar: "))
qtd = 0
while qtd < qtd_papeis:
    if qtd == 0:
        papel = input(f'Digite o código do papel a ser analisado: ')
    else:
        papel = input(f'\n\nDigite o código do proximo papel a ser analisado: ')
    #req = Request(f'http://fundamentus.com.br/detalhes.php?papel=vale3', headers={'User-Agent': 'Mozilla/5.0'})
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

    # procura e acha somente o que for tag td no html
    conteudo = page_soup.find_all("td")

    #declaração das variáveis
    vetor = []
    lucro = []
    i = 0
    v = 0
    cotacao_atual = ptr_liquido = luc_liquido_tri = luc_liquido_anual = qtde_acoes = 0

    #percorrendo o html e encontrando os dados
    for element in conteudo:
        for n in element:
            v = n
        for c in v:
            a = c
            vetor.append(a)

    for element in vetor:
        if element == 'Cotação':
            cotacao_atual = vetor[i+1]
        if element == 'Lucro Líquido':
            lucro.append(vetor[i+1])
        if element == 'Patrim. Líq':
            ptr_liquido = vetor[i+1]
        if element == 'Nro. Ações':
            qtde_acoes = vetor[i+1]

        i += 1
    # como tem 2 lucro liquido no site, coloquei em um vetor e cada elemento corresponde ao periodo
    luc_liquido_anual = lucro[0]
    luc_liquido_tri = lucro[1]

    # imprime os resultados
    print(f'Cotacao: {cotacao_atual}')
    print(f'Patrím. Líquido: {ptr_liquido}')
    print(f'Lucro Liquido 3 Meses: {luc_liquido_tri}')
    print(f'Lucro Liquido 12 Meses: {luc_liquido_anual}')

    ptr_liquido = ptr_liquido.replace('.', '')
    cotacao_atual = cotacao_atual.replace(',', '.')
    luc_liquido_anual = luc_liquido_anual.replace('.', '')
    luc_liquido_tri = luc_liquido_tri.replace('.', '')
    qtde_acoes = qtde_acoes.replace('.', '')

    # transforma em float as strings recebidas
    ptr_liquido = float(ptr_liquido)
    cotacao_atual = float(cotacao_atual)
    qtde_acoes = float(qtde_acoes)
    luc_liquido_anual = float(luc_liquido_anual)
    luc_liquido_tri = float(luc_liquido_tri)

    #imprime os resultados já com seus tipos corretos
    #print(f'Cotacao: {cotacao_atual}')
    #print(f'Patrím. Líquido: {ptr_liquido}')
    #print(f'Lucro Liquido 3 Meses: {luc_liquido_tri}')
    #print(f'Lucro Liquido 12 Meses: {luc_liquido_anual}')


    # Calculos Contábeis
    # Calculo do VPA
    # valor por ação - divide o valor do patrimonio liquido pela quantidade de acões disponíveis,
    # caso seja vendida esse é o valor recebido por ação
    vpa = ptr_liquido / qtde_acoes

    # Calculo de lucro por ação - lucro liquido da empresa dividido por ação será o que cada acionista recebera
    # caso a empresa entregue _todo seu lucro aos acionistas
    lpa = luc_liquido_anual / qtde_acoes

    # P/L
    # O P/L
    # nada mais é do que o preço atual da ação, dividido pelo lucro por ação. Em outras palavras,
    # ele mostra quanto que os investidores estão dispostos a pagar por cada R$ 1 de lucro que a empresa tiver.
    pl = cotacao_atual / lpa

    # rpl quanto uma empresa gera de lucro sobre o seu próprio patrimonio em 12 meses
    rpl = luc_liquido_anual / ptr_liquido
    # multiplica por 100 e teremos a % ao ano
    rpl = rpl * 100

    # dados de acordo com o retorno dos cálculos
    print()
    print(f'Valor por ação (VPA):{vpa:.2f}')
    print(f'Lucro por ação (LPA):{lpa:.2f}')
    print(f'O P/L da {papel} está em {pl:.2f}')
    print(f'Hoje {papel.upper()} gera lucro sobre o seu próprio patrimonio em 12 meses de: {rpl:.2f}%  ')
    qtd = qtd + 1
