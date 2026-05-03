# 1 Soma Total: Crie uma matriz 3 x 3 de números inteiros e exiba a soma de todos os elementos.
# import numpy as np
# x = (np.random.rand(3, 3) * 100).astype(int)
# y = x.sum()
# print(x)
# print(y)

# 2 Identidade: Peça ao usuário um valor n e gere uma Matriz Identidade de ordem n.
# n = int(input("Digite o valor de n: "))
# import numpy as np
# x = np.eye(n)
# print(x)

# 3 Busca Simples: Dada uma matriz 4 x 4, peça um número ao usuário e diga se esse número está ou não na matriz.
# import numpy as np
# n = int(input("Digite o valor de n: "))
# x = (np.random.rand(4, 4) * 100).astype(int)
# if n in x: 
#     print(f"O número {n} está presente na matriz")
# else:
#     print(f"O número {n} não está presente na matriz")

# 4 Troca de Valores: Crie uma matriz 2 x 2 e troque os valores da primeira linha com os da segunda linha.
# import numpy as np
# (x = np.random.rand(2, 2) * 100).astype(int)
# print("Original: \n", x)
# x[[0, 1]] = x[[1, 0]]
# print("Modificada: \n", x)

# 5 Multiplicação por Escalar: Leia uma matriz 3 x 3 e um número real. Exiba a matriz resultante da multiplicação de cada elemento por esse número.
# import numpy as np
# x = (np.random.rand(3, 3) * 100).astype(int)
# n = float(input("Digite um número real: "))
# result = z * n
# print("Matriz Original: \n", x)
# print("Matriz Resultante: \n", result)

# 6 Contagem de Pares: Dada uma matriz 3 x 4, conte quantos números pares ela possui.
# import numpy as np  
# x = (np.random.rand(3, 4) *100).astype(int)
# c = sum([j % 2 == 0 for i in x for j in i])
# print(c)
# print(x)

# 7 Maior Elemento: Crie uma matriz preenchida com números aleatórios e encontre qual é o maior valor presente nela.
# import numpy as np
# x = (np.random.rand(5, 5) * 100).astype(int)
# print(x.max())            

# 8 Média por Linha: Crie uma matriz 3 x 3 e exiba a média aritmética dos valores de cada linha separadamente
# import numpy as np
# x = (np.random.rand(3, 3) *100).astype(int)
# z = x.mean()
# print(z)
# print(x)

# 9 Soma da Diagonal Principal: Calcule a soma de todos os elementos que compõem a diagonal principal de uma matriz 4 x 4.
# import numpy as np
# x = np.random.randint(0, 100, (4, 4))
# print("Matriz 4x4:\n", x)
# print("Soma da diagonal principal:", np.trace(x))

# 10 Matriz Transposta: Escreva um programa que receba uma matriz M x N e gere a sua transposta (N x M).
# import numpy as np
# m = int(input("Digite o número de linhas (M): "))
# n = int(input("Digite o número de colunas (N): "))
# x = (np.random.rand(m, n) * 100).astype(int)
# ts = x.T
# print("Matriz Original:\n", x)
# print("Matriz Transposta:\n", ts)

# 11 Soma de Colunas: Crie uma matriz 3 x 3 e gere uma lista (array) de 3 elementos onde cada elemento é a soma de uma coluna da matriz
# import numpy as np
# x = np.random.randint(0, 100, (3, 3))
# s = np.sum(x, axis=0)
# print("Matriz 3x3:\n", x)
# print("Soma das colunas:\n", s)

# 12 Verificação de Simetria: Verifique se uma matriz quadrada é simétrica (onde a matriz é igual à sua transposta).
# import numpy as np
# x = np.random.randint(0, 10, (2, 2))
# z = x.T
# if np.array_equal(z, x):
#     print("É uma matriz simétrica")
# else :
#     print("Não é uma matriz simétrica")

# 13 Diagonal Secundária: Exiba apenas os elementos da diagonal secundária de uma matriz 5 x 5.
# import numpy as np
# x = np.random.randint(0, 100, (5, 5))
# print("Matriz 5x5:\n", x)
# print("Diagonal Secundária:\n", np.flip(x).diagonal())

# 14 Multiplicação de Matrizes: Implemente a multiplicação de duas matrizes. Lembre-se: para multiplicar A por B, o número de colunas de A deve ser igual ao número de linhas de B.
# import numpy as np 
# x = np.random.randint(0 , 10 , (3, 3))
# y = np.random.randint(0 , 10 , (3, 3))
# c = x @ y
# print(c)

# 15 Rotação 90°: Crie um algoritmo que rotaciona uma matriz quadrada n x n em 90 graus no sentido horário (sem usar bibliotecas prontas como NumPy)
import numpy as np
x = np.random.randint(0,100, (3,3))
n = len(x)
print(x)
for i in range(n):
    for j in range(i, n):
        x[i][j] , x[j][i] = x[j][i], x[i][j]
for i in range(n):
    x[i] = x[i][::-1]
print(x)