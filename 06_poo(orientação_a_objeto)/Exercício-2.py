class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def ler(self, paginas):
        self.paginas_lidas += paginas
        # Garante que páginas lidas não ultrapassem o total
        if self.paginas_lidas > self.total_paginas:
            self.paginas_lidas = self.total_paginas

    def porcentagem_lida(self):
        return (self.paginas_lidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def terminou(self):
        return self.paginas_lidas >= self.total_paginas


# --- Programa Principal ---

# Criando dois livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 300)

# Simulando leituras no Livro 1
print("=== LIVRO 1 ===")
livro1.ler(64)
print(f"Porcentagem lida: {livro1.porcentagem_lida():.1f}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou? {livro1.terminou()}")

print("\nLendo mais 192 páginas...")
livro1.ler(192)
print(f"Porcentagem lida: {livro1.porcentagem_lida():.1f}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou? {livro1.terminou()}")

# Simulando leituras no Livro 2
print("\n=== LIVRO 2 ===")
livro2.ler(150)
print(f"Porcentagem lida: {livro2.porcentagem_lida():.1f}%")
print(f"Páginas restantes: {livro2.paginas_restantes()}")
print(f"Terminou? {livro2.terminou()}")