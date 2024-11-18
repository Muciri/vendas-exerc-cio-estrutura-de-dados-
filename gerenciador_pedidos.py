from product import Produto
from pedido_OO import pedido


class GerenciadorPedidos:
    def __init__(self):
        self.repositorio_pedidos = {}
    
    def pesquisar(self, id:int)->Produto:
        return self.repositorio_produtos.get(id)

    def __str__(self)->str:
        s = ''
        # {self.repositorio_produtos}"""
        for produto in self.repositorio_produtos.values():
            s += produto.__str__() + ', '
        return s
    
    def __len__(self)->int:
        return len(self.repositorio_produtos)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)