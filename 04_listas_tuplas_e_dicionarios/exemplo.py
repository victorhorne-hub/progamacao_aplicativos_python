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