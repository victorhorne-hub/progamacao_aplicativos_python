class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.nivel = 1

    def receber_dano(self, valor):
        self.vida -= valor
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")

    def curar(self, valor):
        if self.vida > 0:
            self.vida += valor
            if self.vida > 100:
                self.vida = 100

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100

    def status(self):
        print(f"Nome: {self.nome} | Classe: {self.classe} | Nível: {self.nivel} | Vida: {self.vida}/100")


# --- Aventura Simula ---

p1 = Personagem("Aragorn", "Guerreiro")
p2 = Personagem("Gandalf", "Mago")

print("=== INÍCIO DA AVENTURA ===")
p1.status()
p2.status()

print("\n--- Ações do Aragorn ---")
p1.receber_dano(40)
print(f"Aragorn após sofrer dano:")
p1.status()

p1.curar(20)
print(f"Aragorn após se curar:")
p1.status()

p1.subir_nivel()
print(f"Aragorn após subir de nível:")
p1.status()

print("\n--- Ações do Gandalf ---")
p2.receber_dano(60)
p2.receber_dano(50) # Deve zerar a vida e mostrar que foi derrotado

print("\n=== STATUS FINAL ===")
p1.status()
p2.status()