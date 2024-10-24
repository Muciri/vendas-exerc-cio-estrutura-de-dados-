from produto import *

serial_pedido = 0 # variável global que vai controlar o ID dos pedidos

dados = {"produtos": [],
         "pedidos": []}

def gerar_id_pedido()->int:
    global serial_pedido
    serial_pedido += 1
    return serial_pedido


def cadastrar_pedido(carrinho:list, valor:float):
    global dados
    dados['pedidos'].append({
        'id': gerar_id_pedido(),
        'items': carrinho,
        'valor': valor}
    )

def pesquisar_pedido(id:int)->dict:
    global dados
    for pedido in dados['pedidos']:
        if pedido['id'] == id:
            return pedido
    return None

def fazer_pedido():
    dados['produtos'] = atualizar_produtos()

    carrinho=[]
    total_compras=0

    while True:
        listar_produtos()
        pedido=input('Digite o Id para escolher um pedido ou digite 0(numero zero)para finalizar compra.')
        print('--------')
        
        if pedido=='0':
            print('Os produtos que voce comprou:')
            for prod in carrinho:
                print(f'{prod["descricao"]},R${prod["valor"]:.2f}')
            print(f'Valor total das suas comprinhas:{total_compras:.2f}')
            print('--------')
            break
        else:
            for produto in dados['produtos']:
                if produto['id']==int(pedido):
                    quant = int(input('Digite quantos produtos desse ID você deseja: '))
                    print('--------')
                    carrinho.append(produto)
                    total_compras += (produto['valor']*quant)

                    carrinho.append({
                        'descricao': produto['descricao'],
                        'valor': produto['valor'],
                        'quantidade': quant
                        })
                    print(f"{quant} x {produto['descricao']} adicionado ao carrinho.")
                    print('--------')
        
    cadastrar_pedido(carrinho, total_compras)

