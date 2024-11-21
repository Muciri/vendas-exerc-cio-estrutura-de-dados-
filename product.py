class Produto:
    __serial = 0
    # método especial denominado "construtor", que é rodado
    # implicitamente toda vez que uma instrução de criação
    # de objeto é encontrado
    def __init__(self, descricao:str, valor:float):
        self.__descricao = descricao
        self.__valor = valor
        Produto.__serial += 1
        self.__id = Produto.__serial

    @property
    def id(self):
        return self.__id
    
    @property
    def descricao(self):
        return self.__descricao
    
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
        Produto: {self.__descricao}
        Valor: {self.__valor:.2f}"""

