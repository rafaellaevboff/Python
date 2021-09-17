print("Você é considerado maior de idade no Brasil? Preencha os dados abaixo para saber!")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade <18:
    print("Você NÃO é considerado maior de idade no Brasil.")

if idade >= 18:
    print("Você É considerado maior de idade no Brasil.")

print("Obrigada por utilizar o programa {}!".format(nome))
