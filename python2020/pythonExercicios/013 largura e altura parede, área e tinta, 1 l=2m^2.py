b = float(input('Qual a largura da sua parede? '))
c = float(input('Qual a altura da sua parede? '))
a = b * c
t = (a / 2)
print('A dimensão da sua parede é {} x {} e a área é {} metros.'.format(b, c, a))
print('Se quiser pintá-la irá precisar de {} litros de tinta'.format(t))
