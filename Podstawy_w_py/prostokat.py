bok1= float(input('Podaj bok 1 \n'))
while bok1<0:
    bok1 = float(input('Podaj dodatnią wartość \n'))
bok2= float(input('Podaj bok 2 \n'))
while bok2<0:
    bok2 = float(input('Podaj dodatnią wartość \n'))
print('Pole tego prostokata to : ', bok1*bok2)
print('Obwod tego prostokata to : ', 2*bok1+2*bok2)

print(f'Dla prostokata o bokach {bok1:.3f} i {bok2:.3f} pole wynosi: {bok1*bok2:.3f} a obwod {2*bok1+2*bok2:.3f}')
