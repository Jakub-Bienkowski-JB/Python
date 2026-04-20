dlugosc = float(input('Podaj dlugosc w cm\n'))
while dlugosc < 0:
    dlugosc = float(input('Podaj dodatnią wartość w cm\n'))
szerokosc = float(input('Podaj szerokosc w cm \n'))
while szerokosc < 0:
    szerokosc = float(input('Podaj dodatnią wartość w cm\n'))
wysokosc = float(input('Podaj wysokosc w cm\n'))
while wysokosc < 0:
    wysokosc = float(input('Podaj dodatnią wartość w cm\n'))

if szerokosc > 50 or dlugosc > 50 or wysokosc > 50 or wysokosc * szerokosc * dlugosc > 50000:
    if szerokosc > 50:
        print(f'bagaz jest za szeroki o {szerokosc - 50}  cm')
    if dlugosc > 50:
        print(f'bagaz jest za dlugi o {dlugosc - 50}  cm')
    if wysokosc > 50:
        print(f'bagaz jest za wysoki o {wysokosc - 50}  cm')
    if wysokosc * szerokosc * dlugosc > 50000:
        print(f'bagaz jest za objetościowy o {wysokosc * szerokosc * dlugosc - 50000}  cm')
else:
    print('Bagaż jest akceptowalny')
