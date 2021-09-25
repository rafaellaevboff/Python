a = float(input('Qual é o salário do funcionário? R$'))
s = (a*1.15)
print('O salário teve um aumento de 15% esse mês, ao invés de ganhar R${:.2f}, irá ganhar R${:.2f}.'.format(a, s))
