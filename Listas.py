#lista de exercicios sobre listas e vetores
#1.Crie uma lista com os números de 1 a 5 e imprima-a na tela
#x = list(range(1, 6))
#print(x)

# 2 Dada a lista cores = ['vermelho', 'azul', 'verde', 'amarelo'], acesse e imprima asegunda cor da lista.
#x = ["vermelho", "azul", "verde", "amarelo"]
#print(x[1])

# 3 Adicione o número 10 ao final da lista numeros = [1, 2, 3].

# x = list(range(1,4))
# x.append(10)
# print(x)

# 4 Remova a palavra "banana" da lista frutas = ['maçã', 'banana', 'laranja']
# x = ['maça', 'banana', 'laranja']
# del(x[1])
#print(x)

#5  Encontre e imprima o tamanho (quantidade de elementos) da lista itens = [10,20, 30, 40, 50].
# x = list(range(10,60,10))
# print(len(x))

# 6 Verifique se o número 7 está presente na lista valores = [1, 3, 5, 7, 9] e imprima o resultado booleano.

#x = list(range(1, 10, 2))
#print(7 in x)

# 7 Concatene as listas lista1 = [1, 2] e lista2 = [3, 4] em uma terceira lista.
# x = list(range(1, 3))
# y = list(range(3, 5))
# z = x + y
# print(z)

# 8 Inverta a ordem dos elementos da lista letras = ['a', 'b', 'c', 'd'].
# x = ['a','b','c','d']
# opt.1 print(x.reverse(), x)
# opt.2 print(x[::-1])
# opt.3 : 
# x.reverse()
# print(x)

#9 Conte quantas vezes o número 2 aparece na lista numeros = [1, 2, 2, 3, 2, 4].

# x = list([1,2,2,2,3,4])
# z= x.count(2)
# print(z)

#10 Calcule e imprima a soma de todos os elementos da lista precos = [10.5, 20.0, 15.5].

# x = [10.5, 15.5, 20.0]
# print(sum(x))

# 11 Escreva um programa que remova as duplicatas de uma lista, garantindo que a ordem original dos primeiros elementos encontrados seja mantida.
# x = [1,1,2,3,4,4,5,6,7,8,6,6,6,7,7,7,9,10]
# z = list(set(x))
# print(z)

# 12 Encontre o maior e o menor número em uma lista de inteiros sem usar as funções nativas max() e min().

# x = list(range(-100000, 100000, 150))
# mn = min(x)
# mx = max(x)
# print(f"minimo: {mn}")
# print(f"maximo: {mx}")

# 13 .Use list comprehension (compreensão de listas) para criar uma lista contendo os quadrados dos números de 1 a 10.

# x = list(n **2 for n in range(1, 11))
# print(x)

# 14 Dada uma lista mista de números, crie uma nova lista contendo apenas os números ímpares da lista original.
# z = list(range(1, 22))
# x = list(n for n in z if n % 3 == 0)
# print(z)
# print(x)

# 15 Escreva um programa que rotacione os elementos de uma lista para a direita em n posições (Exemplo: a lista [1, 2, 3, 4, 5] com n=2 vira [4, 5, 1, 2, 3]).
# x = list(range(1, 11))
# n = int(input("Digite um número: "))
# print(x)
# print(x[-n:] + x[:-n])

# 16 Dadas duas listas, encontre a interseção entre elas (os elementos que estão presentes em ambas) sem usar a conversão para conjuntos (set).
# x = [1, 2,3,4,5,6,7,8,9,10]
# y = [1,3,5,7,9,11]
# z = [n for n in x if n in y]
# print(z)

# 17 "Achate" (flatten) uma lista de listas (uma matriz bidimensional) em uma única lista unidimensional (Exemplo: [[1, 2], [3, 4]] vira [1, 2, 3, 4]).
# x = [[1,2], [3,4], [5,6], [7,8], [9,10]]
# x1 = [n for y in x for n in y]
# print(x1)


# 18 Implemente o algoritmo de ordenação Merge Sort (Ordenação por Mistura) para ordenar uma lista desordenada de números em ordem crescente.
# import heapq as m
# def x(n):
#     if len(n) <= 1:
#         return n
#     z = len(n) // 2
#     E = x(n[:z])
#     D = x(n[z:])
#     return m(E, D)
# def m(E, D):
#     r = []
#     i = j = 0
#     while i < len(E) and j < len(D):
#         if E[i] < D[j]:
#             r.append(E[i])
#             i += 1
#         else:
#             r.append(D[j])
#             j += 1
#     r.extend(E[i:])
#     r.extend(D[j:])
#     return r
# m = input("Digite uma lista de números separados por vírgula: ")
# n = [int(x) for x in m.split(",")]
# print(x(n))

# 19 Dada uma lista de números inteiros (positivos e negativos), encontre a sublista contígua com a maior soma e retorne o valor dessa soma (Algoritmo de Kadane).
# def x(n):
#     ma = mg = n[0]
#     for i in n[1:]:
#         ma = max(i, ma + i)
#         mg = max(mg, ma)
#     return mg
# m = input("Digite uma lista de números separados por vírgula: ")
# ns = [int(x) for x in m.split(",")]
# print(x(ns))

# 20 Escreva uma função recursiva que receba uma lista de números distintos e retorne todas as permutações possíveis de seus elementos.   
# def perm(x):
#    if len(x) <= 1:
    #    return[x]
#    perms = []
    # for i in range(len(x)):
        # z = x[i]
        # c = x[:i] + x[i+1:]
        # for b in perm(c):
            # perms.append([z] + b)
    # return perms
# n = [1, 2, 3]
# ns = perm(n)
# print(len(ns))
# for b in ns:
    # print(b)