from pprint import pprint
# from class_produto import Produto, GerenciarProduto 
from pedido import *
from save import abrir_json, salvar_produtos
from product import Produto
from gerenciador_produtos import *
from pedido_OO import *

dados = abrir_json()
gerenciador = GerenciarProduto(dados)
print(
    "Bem vindo ao nosso sistema de vendas! Aqui você poderá cadastrar produtos e fazer pedidos."
)
print()


# Inicio do programa
while True:
    print("--------")
    opcao = int(
        input(
            """Selecione uma das opções abaixo:
1 - Cadastrar produto.
2 - Listar produtos.  
3 - Fazer pedido.
4 - Pesquisar produtos. 
5 - Exibir pedido                    
6 - Sair.
------------------------------
Opcao: """)
    )
    print("--------")
    if opcao == 1:
        id = int(input('qual o id?'))
        descricao = input('qual a descricao?')
        valor = float(input('qual o valor?'))
        novo_produto = produto(id, descricao, valor)
        GerenciadorProdutos.adicionar_produto(novo_produto)

    elif opcao == 2:
        GerenciadorProdutos.listar_produtos()


    elif opcao == 3: # fazer o pedido

        carrinho=[] # um list vazio, para adicionar os produtos
        # total_compras=0

        while True:
            gerenciador.listar_produtos()
            idProduto = int(input(
                "Digite o Id do produto para adicionar ao carrinho ou digite 0(numero zero)para finalizar compra."
            ))
            print("--------")

            if idProduto == 0:
                print("Os produtos que voce comprou:")
                exibir_pedido(carrinho)

                pergunta = input("Confirmar a compra? (s/n) ")
                if pergunta == "s":
                    id_pedido = fechar_pedido(colecao_pedidos, carrinho)
                    print('Pedido numero ', id_pedido)
                    print("Compra finalizada!")
                break
               

            else:
                produto = gerenciador.pesquisar_produto(idProduto)
                if produto is None:
                    print("Produto não encontrado.")
                    break
                
                # se passar do if, o produto foi recuperado
                quant = int(input("Digite quantos produtos desse ID você deseja: "))
                print("--------")

                add_produto_carrinho(carrinho, idProduto, quant)
                print(f'Produto id={idProduto} adicionado')
                        
    elif opcao == 4:
        pesquisa = int(input('qual o id do produto?'))
        GerenciadorProdutos.pesquisar(pesquisa)

    elif opcao == 5: ## exibir pedido
        pedido.exibir_pedido(carrinho)

    elif opcao == 6:
        print("Fim do programa.")
        print("--------")
        break