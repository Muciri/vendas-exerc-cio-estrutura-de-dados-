from pprint import pprint
from produto import *
from pedido import * 

print('Bem vindo ao nosso sistema de vendas! Aqui você poderá cadastrar produtos e fazer pedidos.')
print()


# Inicio do programa
while True:
    print('--------')
    opcao = int(input('''Selecione uma das opções abaixo:
1 - Cadastrar produto.
2 - Listar produtos.  
3 - Pesquisar produtos.
4 - Fazer Pedido.  
5 - Pesquisar Pedidos.                                         
6 - Sair.
'''))
    
    match opcao:
        case 1:
            descricao, valor = ler_produto()
            cadastrar_produto(descricao, valor)
            print("Produto cadastrado!")
            print('--------')
        case 2:
            listar_produtos()
        case 3:
            id_produto = int(input('Digite o id do produto'))
            retorno_produto = pesquisar_produto(id_produto)
            if retorno_produto:
                print(f"Produto encontrado: {retorno_produto['descricao']}, valor: {retorno_produto['valor']:.2f}")
            else:
                print("Produto não encontrado.")
        case 4:
            fazer_pedido()
        case 5:
            id_pedido = int(input('Digite o id do pedido'))
            retorno_pedido = pesquisar_pedido(id_pedido)
            if retorno_pedido:
                print(f"pedido encontrado: {retorno_pedido['items']}, valor: {retorno_pedido['valor']:.2f}")
            else:
                print("pedido não encontrado.")
        case 6:
            print("Fim do programa.")
            print('--------')
            break
        case _:
            print('resposta inválida')

            

