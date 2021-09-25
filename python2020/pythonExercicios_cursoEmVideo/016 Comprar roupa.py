r = float(input('Qual o valor da roupa que você escolheu? R$'))
dezpc = r*0.90
parc = r*1.08
print(' A roupa que você escolheu custa R${}.'.format(r), end=' ')
print('Se pagar a vista ganha 10% de desconto e ela sairá por R${}.'.format(dezpc))
print('Se parcelar, aumenta em 8% o valor e passará a custar R${}.'.format(parc)) 
