# listas, tuplas e dicionários
from operator import index

#1. Listas

#listas são utilizadas poara armazenar vários valores dentro de uma única variável

nomes = ["Ana","Carlos","João","Maria"]
print(nomes)

#2. Acessando elementos da lista

print(nomes[0])
print(nomes[1])
print(nomes[2])

# Podemso acessar o último elemento da lista -1
print(nomes[-1])

# 3. Alterando os elementos

# As listas são mutáveis, ou seja: Os elementos podem mudar
nomes[0]="Pedro"
print(nomes)

# 4. Adicionando elementos
#append() adiciona um elemneto no final da lista.
nomes.append("Lucas")
print(nomes)

# insert() adicina um eleento em uma posição
nomes.insert(1,"Jubesvaldo")
print(nomes)

#5. Removendo Elementos
#remove() remove um elemento pelo valor
nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo índice
nomes.pop(0)
print(nomes)

# 6. tamanho da lista

# len() informa a quantidade de elementos


# 7.percorrendo uma lista
for noem in nomes:
    print(nome)

# 8. Verificando se um elemento existe

if "João" in nomes:
    print("João está na lista")
else:
    print("joão não esta na lista")


# 9. Lista com diferentes tipos de dados

dados= ["João",18,1.75,true]
print(dados)

# 10. Lista de números
notas = [7.5,8.0,6.5,9.0]
soma = 0

for nota in notas:
    soma += nota

media = soma/len(notas)
print(f"Média: {media:.1f}")

# 11. Tuplas
# Tuplas são semelhantes às listas.
# A principal diferença é que tuplas não podem ser alteradas depois de criadas

cordenadas = (10,20)
print(cordenadas)

# Acessando elementos.
print(cordenadas[0])
print(cordenadas[1])

# 12. Dicionários
# Dicionários armazenam informações no formato:
# chave: valor

aluno = {
    "nome": "Carlos",
    "Idade": 18,
    "Nota": 8.5
}
print(aluno)

# 13. Acessando valores do dicionário

print(aluno["Nome"])
print(aluno["Idade"])
print(aluno["Nota"])

# 14. Alterando valores
aluno["Nota"] = 9.0
print(aluno)