wiersz=int(input("Podaj liczbe wierszy "))
kolumny=int(input("Podaj liczbe kolumn "))
szer=len(str(wiersz*kolumny))+1
for i in range (1, kolumny+1):
    print()
    for j in range (1, wiersz+1):
        print(f'{i*j:{szer}}', end=' ')
