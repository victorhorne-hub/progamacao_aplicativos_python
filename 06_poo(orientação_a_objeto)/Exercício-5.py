class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def subtotal(self):
        return self.preco * self.quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def total(self):
        return sum(produto.subtotal() for produto in self.itens)

    def mostrar(self):
        print("=== COMPRAS NO CARRINHO ===")
        for prod in self.itens:
            print(f"- {prod.nome} (R$ {prod.preco:.2f} x {prod.quantidade}): R$ {prod.subtotal():.2f}")
        print("---------------------------")
        print(f"TOTAL DA COMPRA: R$ {self.total():.2f}")


# --- Programa Principal ---

# Criando 4 produtos
p1 = Produto("Arroz 5kg", 24.90, 2)
p2 = Produto("Feijão 1kg", 8.50, 3)
p3 = Produto("Leite 1L", 4.20, 6)
p4 = Produto("Café 500g", 16.00, 1)

# Criando o carrinho e adicionando os produtos
meu_carrinho = Carrinho()
meu_carrinho.adicionar(p1)
meu_carrinho.adicionar(p2)
meu_carrinho.adicionar(p3)
meu_carrinho.adicionar(p4)

# Exibindo o resumo da compra
meu_carrinho.mostrar()