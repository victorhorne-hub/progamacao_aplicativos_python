# O que é uma função:
# Bloco de código criado para realizar uma tarefa específica, organizando e reutilizando o código.

# 1. Criando e chamando uma função simples
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()

# 2. Função com parâmetro
def saudacao_pessoa(nome):
    print(f"Olá, {nome}")

# As chamadas ficam fora da função
saudacao_pessoa("Ana")
saudacao_pessoa("Carlos")

# 3. Mais de um parâmetro (com argumentos nomeados)
def apresentar(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar(nome="Ana", idade=20)

# 4. Função com cálculo (imprimindo direto)
def somar_e_mostrar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

somar_e_mostrar(10, 5)

# 5. Retornando um valor (return)
def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10, 5)
print(resultado)

# 6. Função com condição (if / else)
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificar_idade(20))

# 7. Valor padrão para parâmetro
def saudacao_visitante(nome="Visitante"):
    return f"Olá, {nome}!"

print(saudacao_visitante())         # Usa o valor padrão "Visitante"
print(saudacao_visitante("Maria"))  # Sobrescreve com "Maria"

# 8. Organizando o programa com funções
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: "))
    return nome, preco

def exibir_produto(nome, preco):
    print("\n=== PRODUTO ===")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco}")

# Fluxo principal do programa (fora das funções)
nome_prod, preco_prod = cadastrar_produto()
exibir_produto(nome_prod, preco_prod)

































































































































































































































































































































































































