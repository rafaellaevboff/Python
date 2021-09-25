from random import shuffle
a01 = str(input("Digite o nome do 1º aluno: "))
a02 = str(input("Digite o nome do 2º aluno: "))
a03 = str(input("Digite o nome do 3º aluno: "))
a04 = str(input("Digite o nome do 4º aluno: "))
lista = [a01, a02, a03, a04]
shuffle(lista)
print("A ordem das apresentações será: {}".format(lista))