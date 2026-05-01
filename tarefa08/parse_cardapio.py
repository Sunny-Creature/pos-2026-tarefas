from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    id = prato.getAttribute('id')
    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    print(f'{id}- {nome}')
    
    opcao_prato = input("Digite o ID de um prato:")

    if opcao_prato == prato.getAttribute('id'):
        elemento_descricao = prato.getElementsByTagName('descricao')[0]
        descricao = elemento_descricao.firstChild.nodeValue
        ingrediente = prato.getElementsByTagName('ingrediente')
        elemento_preco = prato.getElementsByTagName('preco')[0]
        preco = elemento_preco.firstChild.nodeValue
        elemento_calorias = prato.getElementsByTagName('calorias')[0]
        calorias = elemento_calorias.firstChild.nodeValue

    print('-'*10)
    print("Nome:", nome)
    print("Descrição:", descricao)
    print("Ingredientes:")
    for ingrediente in ingrediente:
        print(ingrediente.firstChild.nodeValue)
    print("Preço:", f'R${preco}')
    print("Calorias:", calorias)