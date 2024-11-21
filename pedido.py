class Pedido:
    __serial = 0
    def __init__(self, carrinho:list, valor:float):
        self.__carrinho = carrinho
        self.__valor = valor
        Pedido.__serial += 1
        self.__id = Pedido.__serial

    @property
    def id(self):
        return self.__id
    
    @property
    def carrinho(self):
        return self.__carrinho
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor:float):
        if valor > 0.0:
            self.__valor = valor
        
    
    def set_preco(self, percentual:float):
        if percentual > 0.0:
            self.__valor += self.__valor * percentual / 100

    def __str__(self)->str:
        return f""" PRODUTO DISPONÍVEL
        Id: {self.__id}
        carrinho: {self.__carrinho}
        Valor: {self.__valor:.2f}"""