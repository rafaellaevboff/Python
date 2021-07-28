a = float(input('Qual o preço do seu produto? R$'))
p = (a*0.95)
print('Seu produto, que antes era R${}, está custando R${:.1f}, pois está com 5% de desconto.'.format(a, p))