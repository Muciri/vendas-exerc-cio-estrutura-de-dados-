class ItemPedido:
    def __init__(self, id_produto: int, quantidade: int):
        self.__id_produto = id_produto
        self.__quantidade = quantidade
    
    def __str__(self):
        return f'id: {self.id_produto}, quantidade: {self.quantidade}'
    
    @property
    def id_produto(self):
        return self.__id_produto

    @property
    def quantidade(self):
        return self.__quantidade