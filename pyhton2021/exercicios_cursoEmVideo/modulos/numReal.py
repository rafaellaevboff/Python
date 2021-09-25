from math import trunc

x = float(input("Digite um número com vírgula e 4 números após ela: "))

print("O número digitado foi {}, sua porção inteira é: {}.".format(x, trunc(x)))
