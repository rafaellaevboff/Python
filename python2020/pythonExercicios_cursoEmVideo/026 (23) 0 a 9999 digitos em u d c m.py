num = int(input('Digite um número que esteja entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Análisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(c))
print('Centena: {}'.format(d))
print('Milhar: {}'.format(m))
