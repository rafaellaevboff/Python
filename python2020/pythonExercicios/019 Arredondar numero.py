from math import trunc
a = float(input('Digite um número com casas decimais: '))
print('A porção inteira de {} é {}'.format(a, trunc(a)))

# ou

b = float(input('Digite um número com casas decimais: '))
print('A porção inteira de {} é {}'.format(a, int(a)))
