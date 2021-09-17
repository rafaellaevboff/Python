print("Vamos somar idades. Para parar de somar digite o número 0.")

idade = 0
somaIdade = 0
i = 0
while True:
    i = i + 1
    idade = int(input("Digite a {}ª idade: ".format(i)))
    somaIdade = somaIdade + idade
    if idade == 0:
        break
print("A soma das idades é {}.".format(somaIdade))