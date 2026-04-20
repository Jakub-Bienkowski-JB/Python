import random
x=random.randint(1,10)
y=random.randint(1,10)
proba=0
wynik=x*y
while True:
    odpowiedz= int(input(f'ile to jest {x} razy {y}? '))
    proba+=1
    if odpowiedz == wynik:
        print(f'Brawo udalo ci sie w {proba} probie!')
        break
    print('źle sprobuj jeszcze raz ')

