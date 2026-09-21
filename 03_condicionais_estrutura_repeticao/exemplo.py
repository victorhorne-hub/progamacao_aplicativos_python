#1. Estrutura Condicionais

nota = 6

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
        print('Em recuperação')
else:
    print('Reprovado')


    # Cndicionais e operadores lógicos
    #and -> Todas as condicionais devem ser verdadeiras
    #or -> Pelomenos uma condicional deve ser verdadeira


    idade = 20
    ingresso = true

    if idade >= 18 and ingresso:
        print('Entrada aprovada')
    else:
        print('Entrada não permitida')

    #3. estrutura de repetição while
    contador = 1

    while contador <= 5:
        print(contador)
        contador += 1

    # 4. Estrutura de repetição for
    for numero in range(1,6):
        print(numero)

    # 5. Percorrendo uma lista
    nomes = ["Ana","carlos","João","Maria"]
    for nome in nomes:
        print(nome)

    # 6. Break, Continue, pass
    for numero in range(1,11):

        if numero == 6:
            #break
            #continue
            #pass
    print(numero)
