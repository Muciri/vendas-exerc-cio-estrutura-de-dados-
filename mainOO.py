from product import Produto
from gerenciador_produtos import GerenciadorProdutos

p1 = Produto("Cadeira", 100.0)
p2 = Produto("Mesa", 200.0)
p3 = Produto("Cama", 300.0)

print(p1.id)
print(p2.id)
print(p3.id)
print("valor de p1:", p1.valor) # aqui chamamos o método get de valor

p1.valor = -150
print("valor de p1:", p1.valor) # aqui chamamos o método get de valor

gprod = GerenciadorProdutos()
gprod.adicionar_produto(p1)
gprod.adicionar_produto(p2)
gprod.adicionar_produto(p3)
gprod.adicionar_produto(Produto("Sofá", 400.0))
gprod.adicionar_produto(Produto("Almofada", 30.0))



print(gprod)
exit()


# for prod in gprod:
#     print(prod)

print(len(gprod))
print(gprod.pesquisar(31))
print(gprod.remover(3))
print(gprod.count())
exit()

p2.set_preco(-10)
p3.valor = -400
print(p2)
print(p3)
exit()


print(p2)
print(p3)
exit()

print('Antes:', p1)
p1.set_preco(15)
print('Depois:', p1)
print(p2)