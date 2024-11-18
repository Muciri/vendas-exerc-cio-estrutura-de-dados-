from product import Produto
from pedido_OO import pedido


class GerenciadorPedidos:
    def __init__(self):
        self.repositorio_pedidos = {}
    
    def pesquisar(self, id:int)->Produto:
        return self.repositorio_produtos.get(id)
    
    def get_pedido(self):
        return pedido.__str__

    def __str__(self)->str:
        s = ''
        # {self.repositorio_produtos}"""
        for pedido in self.repositorio_pedidos.values():
            s += pedido.__str__() + ', '
        return s
    
    def __len__(self)->int:
        return len(self.repositorio_pedidos)

    def listar_pedidos(self):
        for pedido in self.repositorio_pedidos:
            print(pedido)