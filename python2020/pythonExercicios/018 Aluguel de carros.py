d = int(input('Alugou o carro por quantos dias? '))
k = float(input('E quantos km você rodou com ele? '))
pago = (d*60) + (k*0.15)
print('O valor total do aluguel é R${:.2f}'.format(pago))
