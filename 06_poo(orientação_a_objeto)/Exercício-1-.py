class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Raça: {self.raca} | Idade: {self.idade} anos")


# 1. Criando dois cachorros diferentes
cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)
cachorro2 = Cachorro("Thor", "Golden Retriever", 5)

# 2. Chamando os métodos para o primeiro cachorro
cachorro1.latir()
cachorro1.mostrar_info()

print("-" * 40)

# 3. Chamando os métodos para o segundo cachorro
cachorro2.latir()
cachorro2.mostrar_info()

print("-" * 40)

# 4. Alterando a idade do primeiro cachorro diretamente pelo atributo
cachorro1.idade = 4

# 5. Conferindo a mudança
print("Após alterar a idade do Rex diretamente no atributo:")
cachorro1.mostrar_info()