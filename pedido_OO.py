from save import abrir_json, salvar_produtos
# from gerenciador_produtos import pesquisar 

# estrutura de dados para armazenar todos pedidos
colecao_pedidos = {} #chave=ID;valor=list(carrinho)
# variável controladora do serial do pedido
serial_num_pedido = 0

# carregando dados
dados = abrir_json()
salvar_produtos(dados)

def gerar_id_pedido() -> int:
    global serial_num_pedido
    serial_num_pedido += 1
    return serial_num_pedido

class pedido:
    def __init__(self, id:int, carrinho:list, valor:float):
        self.id = id
        self.carrinho = carrinho
        self.valor = valor
    
    def fechar_pedido(self, colecao_pedidos:dict,)->int:
        id_pedido = gerar_id_pedido()
        colecao_pedidos[id_pedido] = self.carrinho
        return id_pedido
    
    def add_produto_carrinho(self, idProduto:int,quant:int):
        self.carrinho.append([idProduto,quant])

    def exibir_pedido(self):
        print('======================================================')
        print("                 Itens do pedido:")
        print('======================================================')
        print('idProduto  | Descrição      | Preço Unit. | Quantidade')
        print('-----------  ---------------  ------------  ----------')
            
        total = 0
        for item in self.carrinho:
            produto = pesquisar(item[0]) 
            print(f"   {produto['id']:03d}       {produto['descricao']:15s}    {produto['valor']:10.2f}      {item[1]:3d}")
            total += produto['valor'] * item[1]

        print('======================================================')
        print(f"Valor total das suas comprinhas:{total:.2f}")
        print('======================================================')
