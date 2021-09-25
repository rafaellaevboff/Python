import random
a01 = str(input("Digite o nome do 1º aluno: "))
a02 = str(input("Digite o nome do 2º aluno: "))
a03 = str(input("Digite o nome do 3º aluno: "))
a04 = str(input("Digite o nome do 4º aluno: "))
lista = [a01, a02, a03, a04]
aluno_escolhido = random.choice(lista)
print("O aluno(a) escolhido(a) foi {}".format(aluno_escolhido))