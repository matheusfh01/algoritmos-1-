# 1 Crie um dicionário com nome, idade e cidade de uma pessoa. Solicite ao usuário uma chave e exiba o valor correspondente.
# x = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo"
# }

# chave = input("Digite uma chave (nome, idade ou cidade): ")
# print(x.get(chave, "Chave não encontrada."))

# 2 Crie um dicionário com o preço de três produtos. Peça ao usuário qual produto deseja alterar e o novo preço. Atualize o dicionário e exiba o resultado.
# p = {
#     "produto1": 10.0,
#     "produto2": 20.0,
#     "produto3": 30.0
# }
# x = input("Digite o nome do produto que deseja alterar (1, 2 ou 3): ")
# np = float(input("Digite o novo preço: "))
# p[f"produto{x}"] = np
# print(p)

# 3 Crie um dicionário vazio. Solicite ao usuário um nome e uma idade e armazene essas informações no dicionário como chave e valor. Exiba o dicionário ao final.
# d = {}
# z = input("Digite o numero de indivíduos que deseja cadastrar: ")
# for _ in range(int(z)):
#     n = input("Digite o nome: ")
#     i = int(input("Digite a idade: "))
#     d[n] = i
# print(d)

# 4 Peça ao usuário para informar três pares de dados (chave e valor). Utilize a função dict() para construir o dicionário e exiba o resultado.
# x = {}
# for _ in range(3):
#     k = input("Digite a chave: ")
#     v = input("Digite o valor: ")
#     dict.setdefault(x, k, v)
# print(x)

# 5 Crie um dicionário com alguns elementos. Pergunte ao usuário se deseja apagar todos os dados. Caso a resposta seja 'sim', utilize clear() e mostre o dicionário final.
# x = { "chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
# print(x)
# resposta = input("Deseja apagar todos os dados? (s/n): ")
# if resposta == "s":
#     x.clear()
#     print("dicionario apagado: \n", x)
# else: 
#     print("Dicionário não apagado.")

# 6 Crie um dicionário com alguns dados. Faça uma cópia desse dicionário. Em seguida, altere um valor na cópia e mostre os dois dicionários para comparar.
# x = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
# z = x.copy()
# z["chave1"] = "valor 4"
# print("Dicionário original: \n", x)
# print("Dicionário copiado: \n", z)

# 7 Solicite ao usuário uma lista de nomes (separados por vírgula). Utilize fromkeys() para criar um dicionário onde todas as chaves sejam esses nomes e o valor padrão seja 0
# nm = input("Digite uma lista de nomes separados por vírgula: ")
# ns = [n.strip() for n in nm.split(",")]
# d = dict.fromkeys(ns, 0)
# print(d)

# 8 Crie um dicionário com alguns alunos e suas notas. Peça ao usuário o nome de um aluno e utilize get() para buscar a nota. Caso o aluno não exista, exiba uma mensagem padrão.
# als = {
#     "Alice": 85,
#     "Bob": 90,
#     "Charlie": 78
# }
# al = input("Digite o nome do aluno: ")
# n = als.get(al, "Aluno não encontrado.")
# print(f"Nota de {al}: {n}")

# 9 Crie um dicionário com produtos e preços. Mostre ao usuário todas as chaves, todos os valores e todos os pares chave–valor.
# p = {
#     "produto1": 10.0,
#     "produto2": 20.0,
#     "produto3": 30.0
# }
# print("Chaves:", list(p.keys()))
# print("Valores:", list(p.values()))
# print("Pares chave–valor:", list(p.items()))

# 10 Crie um dicionário com alguns dados. Peça ao usuário uma chave para remover usando pop(). Em seguida, remova um item com popitem(). Depois, peça novos dados ao usuário e atualize o dicionário com update(). Exiba o dicionário final.
# d = {
#     "chave1": "valor1",
#     "chave2": "valor2",
#     "chave3": "valor3"
# }
# print(d)
# dr = input("Digite a chave que deseja remover: ")
# d.pop(dr, "Chave não encontrada.")
# d.popitem()
# nk = input("Digite a nova chave: ")
# nv = input("Digite o novo valor: ")
# d[nk] = nv
# print(d)

# 11 Desenvolva um programa em Python que simule um pequeno sistema de gerenciamento de usuários utilizando dicionários.
# usuarios = {
#     "Alice": 30,
#     "Romario": 25,
#     "Luciano": 35
# }

# def info(Opção):
#     if Opção == "1": 
#         dados = input("Oque você quer buscar(nome, idade ou ambos): ")
#         if dados == "nome":
#             for nome in usuarios.keys():
#                 print(nome)
#         elif dados == "idade":
#             for idade in usuarios.values():
#                 print(idade)
#         elif dados == "ambos":
#             for ambos in usuarios.items():
#                 print(f"{ambos[0]}: {ambos[1]}")

#     elif Opção == "2":
#         Busca = input("Digite o nome do usuário para buscar a idade: ")
#         idade = usuarios.get(Busca, "Usuário não encontrado.")
#         print(f"Idade de {Busca}: {idade}")
        
#     elif Opção == "3":
#         novo_usuario = input("Digite o nome do novo usuário e sua idade(separados por vírgula): ")
#         nome, idade = novo_usuario.split(",")
#         usuarios[nome.strip()] = int(idade.strip())
#         print("Dicionário atualizado:", usuarios)
  
#     elif Opção == "4":
#         remove_usuario = input("Digite o nome do usuário que deseja remover: ")
#         usuarios.pop(remove_usuario, "Usuário não encontrado.")
#         print("Dicionário atualizado:", usuarios)
   
#     elif Opção == "5":
#         remove_last = input("Deseja remover o último usuário adicionado? (s/n): ")
#         if remove_last == "s":
#             usuarios.popitem()
#             print("Último usuário removido. Dicionário atualizado:", usuarios)
#         else:
#             print("Dicionário inalterado:", usuarios)
    
#     elif Opção == "6":
#         Copia = input("Deseja criar uma cópia do dicionário? (s/n): ")
#         if Copia == "s":
#             usuarios_copia = usuarios.copy()
#             print("Cópia do dicionário criada:", usuarios_copia)
#         else: 
#             print("Dicionário original mantido:", usuarios)
#         Alterar_copia = input("Deseja alterar um valor na cópia? (s/n): ")
#         if Alterar_copia == "s":
#             Alterar = input("Digite o nome do usuário que deseja alterar e a nova idade(separados por vírgula): ")
#             nome, idade = Alterar.split(",")
#             usuarios_copia[nome.strip()] = int(idade.strip())
#             print("Dicionário original:", usuarios)
#             print("Dicionário copiado e alterado:", usuarios_copia)
#     elif Opção == "7":
#         Nova_dict = input("Digite uma lista de nomes separados por vírgula: ")
#         ns = [n.strip() for n in Nova_dict.split(",")]
#         nova_lista = dict.fromkeys(ns, 18)
#         print("Novo dicionário criado: ", nova_lista)
#     elif Opção == "8":
#         Quantidade = input("Digite a quantidade de itens para o novo dicionário: ")
#         Nova_dict = {}
#         for i in range(int(Quantidade)):
#             k = input("Digite a chave: ")
#             v = input("Digite o valor: ")
#             dict.setdefault(Nova_dict, k, v)
#         usuarios.update(Nova_dict)
#         print("Dicionário atualizado: ", usuarios)
#     elif Opção == "9":
#         Deseja_limpar = input("Deseja limpar o sistema? (s/n): ")
#         if Deseja_limpar == "s":
#             usuarios.clear()
#             print("Sistema limpo.")
#         else: 
#             print("Sistema mantido: ", usuarios)
#     elif Opção == "10":
#         Lista_tuplas = input("Digite uma lista de tuplas (chave : valor) separados por vírgula: ")
#         tuplas = [tuple(item.strip().split(":")) for item in Lista_tuplas.split(",")]
#         novo_dict = dict(tuplas)
#         print("Novo dicionário criado a partir da lista de tuplas: ", novo_dict)
    
#     elif Opção == "0":
#         return False
    
#     else:
#         print("Opção inválida. Por favor, escolha uma opção válida.")
#     return(True)
# while True:
#     Menu = input("""
#                  0. Sair
#                  1. Exibir informações
#                  2. Buscar idade por nome
#                  3. Adicionar novo usuário
#                  4. Remover usuário
#                  5. Remover último usuário adicionado
#                  6. Criar uma cópia e alterar um valor.
#                  7. Criar novo dicionário
#                  8. Atualizar o dicionário principal
#                  9. Limpar sistema
#                  10. Criar novo dicionario apartir de uma lista de tuplas
#                  Digite o número da opção desejada: 
#                  """)
#     Continue = info(Menu)
#     if not Continue:
#         print("Encerrando o programa.")
#         break