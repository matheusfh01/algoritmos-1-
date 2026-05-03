np.random.rand(3,3) = cria matriz aleatória, astype(int) = transforma em inteiro, sum() = soma todos os elementos
np.eye(n) = cria matriz identidade (1 na diagonal, 0 no resto)
n in x = verifica se o número está na matriz
x[[0,1]] = x[[1,0]] = troca as linhas da matriz
x * n = multiplica todos os elementos por um número (⚠️ seu código tem erro: usou z em vez de x)
j % 2 == 0 = verifica se é par, sum(...) = conta quantos são pares
x.max() = encontra o maior valor da matriz
x.mean() = calcula média (⚠️ seu código pega média geral, não por linha; correto seria axis=1)
np.trace(x) = soma a diagonal principal
x.T = gera a matriz transposta (troca linhas por colunas)
np.sum(x, axis=0) = soma os valores de cada coluna
x.T = transposta
np.array_equal(x, x.T) = verifica se é simétrica
np.flip(x) = inverte matriz
.diagonal() = pega diagonal secundária
x @ y = multiplica matrizes
troca x[i][j] com x[j][i] = faz transposição manual, [::-1] = inverte linhas → rotação 90°
