nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome completo em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))