n = float(input('Vamos transformar um número em metros para dm, dam, cm, hm, mm e km. Digite um número para ser convertido: '))
dm = n * 10
dam = n/10
cm = n * 100
hm = n / 100
mm = n * 1000
km = n / 1000
print('{} metros em dm é {}, em cm é {} e em mm é {}'.format(n, dm, cm, mm))
print('{} metros em dam é {}, em hm é {} e em km é {}'.format(n, dam, hm, km))
