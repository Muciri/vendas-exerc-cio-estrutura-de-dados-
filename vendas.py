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
3 - Fazer pedido.
4 - Pesquisar produtos.                     
5 - Sair.
'''))
    print('--------')
    if opcao == 1:
        descricao, valor = ler_produto()
        cadastrar_produto(descricao, valor)
        print("Produto cadastrado!")
        print('--------')

    elif opcao==2:
        listar_produtos()
    
    elif opcao ==3:
        fazer_pedido()

    elif opcao==4:
        id = int(input('Digite o id do produto'))
        retorno = pesquisar_produto(id)
        if retorno:
            print(f"Produto encontrado: {retorno['descricao']}, valor: {retorno['valor']:.2f}")
        else:
            print("Produto não encontrado.")
            
    elif opcao==5:
        print("Fim do programa.")
        print('--------')
        break