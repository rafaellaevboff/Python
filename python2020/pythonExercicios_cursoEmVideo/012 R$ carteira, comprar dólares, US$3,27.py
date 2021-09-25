n = float(input('Quantos reais você tem na carteira? R$'))
c = float(n/3.27)
m = input('O dólar está custando 3,27 reais. Com R${:.2f} você pode comprar US${:.2f}'.format(n, c))
