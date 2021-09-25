frase = str("Ola tudo bem?")
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find("tudo"))
print(frase.find("hoje"))
print("bem" in frase)
print(frase.replace("bem", "ótimo"))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
# somente primeiro caracter em maiúscula, o resto em minúsculas
print(frase.title())

# string grande, tipo texto:
print("""\noi
oi! tudo bem com você?
eu estou bem e vc?
eu também, obg por perguntar""")
