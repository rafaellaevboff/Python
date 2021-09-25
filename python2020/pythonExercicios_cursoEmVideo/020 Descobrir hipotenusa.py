from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

#ou

co = float(input('Digite o tamanho do cateto oposto do seu triângulo: '))
ca = float(input('Digite o tamanho do cateto adjacente do seu triângulo: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa, do triângulo retângulo, resultante dos catetos {:.0f} e {:.0f} é {:.2f}'.format(co, ca, hi))

