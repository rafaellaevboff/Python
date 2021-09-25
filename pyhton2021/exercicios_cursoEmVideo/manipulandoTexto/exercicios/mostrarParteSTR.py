frase = "Vou no mercado."
print("Frase01: " + frase)
print(frase[3:13:2])  # o último elemento(nesse caso o 2) é o intervalo entre um espaço de memória e outro
print(frase[1::2])  # omiti o fim pois "não sei" onde termina
print(frase[::2])  # omiti o começo e fim pois "não sei" onde começa e nem onde termina
print(frase.count('o'))  # o!=O
print(frase.upper().count('O'))  # transformei a frase toda em maiúscula e pedi pra contar quantos o maiúsculo tem
print(frase.replace("mercado", "açougue"))
dividido = frase.split()
print(dividido)
print(dividido[2][3])  # vai pegar o elemento 2 e mostrar a sua 3ª letra
# UMA STRING É IMUTÁVEL

frase02 = "    tudo certo?   "
print("\n Frase02:" + frase02)
print(len(frase02))
print(len(frase02.strip()))
print("olá" in frase02)  #False
print(frase02.find("certo"))
