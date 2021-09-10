a = float(input('Primeiro Bimestre: '))
while a > 10 or a < 0:
    a = float(input('Nota errada. Primeiro Bimestre '))

b = float(input('Segundo Bimestre: '))
while b > 10 or b < 0:
    b = float(input('Nota errada. Segundo Bimestre '))

c = float(input('Terceiro Bimestre: '))
while c > 10 or c < 0:
    c = float(input('Nota errada. Terceiro Bimestre '))

d = float(input('Quarto Bimestre: '))
while d > 10 or d < 0:
    d = float(input('Nota errada. Quarto Bimestre '))

media = (a + b + c + d)/ 4
print('media: {}'.format(media))
