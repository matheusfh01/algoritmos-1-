###1
#def soma(a, b):
#    return a + b
#result = soma(2, 2)
#print(result)

###2
#def mult(a , b):
#    return a * b
#res = mult(2, 4)
#print(res)

###3
#def a(nm):
#    print(f"Bem vindo, {nm}")
#a("matheus")

###4
#def x(a, b):
#    if a > b:
#        print(f"{a} é o maior numero")
#    else:
#        print(f"{b} é o maior numero")
#z = x(int(input("Insira o valor a: ")),  int(input("insira o valor b: ")))

###5
#def x(a, b):
#    q = a // b
#    r = a % b
#    return q, r
#res = x(10, 5)
#print(res)

###6
#def n(a):
#    return a % 2 == 0
#x = n(10)
#print(x)

###7
#def teste():
#   print('Olá')
#resultado = teste()
#print(resultado)
#Ola, none

###8 e 9 e 10
#def f(nome, idade, cidade):
#    print(f"{nome}, {idade}, {cidade}")
#f("matheus", 17, "curitiba")
#f(nome= "matheus", idade= 17, cidade= "curitiba")
#O que acontece em: apresentar('Ana', 'Curitiba', 20)?
#Resposta do sistema = Ana, Curitiba, 17 (a ordem da idade e cidade é invertida

###11 e 12
#def f(nm, p= "dia"):
#    if p == "" :
#        p = "dia"
#    print(f"{nm},bom {p}")
#f("matheus")
#f("matheus", input("Digite o periodo do dia: "))

###13
#def ex(a=1, b):
  # O parametro "a" é considerado o "variavel", oque significa que ele não pode seguir um valor padrão]

###14
#def soma(*numeros):
#    return sum(numeros)
#print(soma(10, 15, 20, 30))

###15
#def md(**dados):
#    for c, v in  dados.items():
#        print(f"{c}, {v}")
#md(nome="matheus", idade= 17,cidade="curitiba")

###16
#*args = multiplos argumentos posicionais
#kwargs = argumentos nomeados

###17
#x = 10
#def teste():
#    x = 5
#print(x)
#resultado = 10

###18
#def incrementar(contador):
 #   if contador == 0:
 #       print("Fim")
 #   else:
 #       print(contador)
#        incrementar(contador - 1)
#incrementar(5)

###19
#T = 0
#def triplo():
#    print(T)
#triplo()

###20
#def executar(funcao, valor):
#    print(executar)

###21
#Q = lambda x: x ** 2
#print(Q(5))

###22
#def Z(n):
#    return  n * 2
#ns = [10, 20, 30, 40, 50]
#x = list(map(Z, ns))
#print(ns)
#print(x)

###23
#n = [1, 2, 3, 4, 5]
#p = filter(lambda n : n % 2 == 0, n)
#print(list(p))

###24
#def f(n):
#    if n == 0 or n == 1:
#        return 1
#    return n * f(n - 1)
#ns = 5
#print(f(ns))

###25
#def cont(n):
 #   if n == 0:
 #       print("Fim")
 #   else:
 #       print(n)
#        cont(n - 1)
#cont(input("Digite o valor da contagem: ")

###26
#def erro(n):
 #   if n == 0 or n == 1:
 #       return 1
#    return n * erro(n - 1)
#print(erro(5))
#Resposta: como n não é imposto um valor limite, a variavel fica infinita

##27 e 28
#def f(**lista):
#    """
#    cria uma lista com a media dos alunos
#    :param lista:
#    :return:
#    """
#    for c, v in  lista.items():
#        print(f"{c}, {v}")
#f(nome= "art", media = 60)
#help()

##29
#def calc(a, b, op):
#    if op == "+":
#        print(a + b)
#    elif op == "-":
#        print(a - b)
#    elif op == "*":
#        print(a * b)
#    else:
#        print(a / b)
#n1 = float(input("insira o valor 1: "))
#n2 = float(input("insira o valor 2: "))
#opp = input("insira qual operação ira ser feita(+, -, * ou /): ")

##30
def pd(*args, **kwargs):
    return args, kwargs