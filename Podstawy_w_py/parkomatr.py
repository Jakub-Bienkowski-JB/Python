godziny = int(input('Podaj godziny : '))
kwota=godziny*4
while kwota>0:
    moneta = int(input(f'Do zaplaty zostalo {kwota} PLN wrzuc monete: '))
    if moneta==1 or moneta==2 or moneta==5:
        kwota-=moneta
    else:
        print('Niepoprawna moneta')

print('Parking opłacony ')
if(kwota<0):
    print(f'Wydano resztę: {-kwota} PLN')
