def ostatnia_cyfra(x):
    return x%10

def suma_cyfr(x):
    suma=0
    while x>0:
        suma+=x%10
        x//=10
    return suma

def najmniejszy_dzielnik(x):
    if x<=1:
        return 1
    for i in range (2,x+1):
        if x%i==0:
            return i
def nwd (x,y):
    if y>x: x,y=y,x
    while y!=0:
        x,y = y, x%y
    return x;
def silnia(x):
    if x==1:
        return 1
    else:
        return x*silnia(x-1)
def silnia_v2(x):
    iloczyn=1
    for i in range(2,x+1):
        iloczyn*=i
    return iloczyn

arg1= int(input('Podaj argument: '))
arg2= int(input('Podaj argument: '))
print('nwd', nwd(arg1, arg2))
print('Podawaj liczby a ja licze wyniki funkcji')
print('Argument -1 konczy program')
while True:
    arg= int(input('Podaj argument: '))
    if arg == -1:
        break
    print('ostatnia_cyfra: ', ostatnia_cyfra(arg))
    print('suma_cyfr: ', suma_cyfr(arg))
    print('najmniejszy dzielnik: ', najmniejszy_dzielnik(arg))
    print('Silnia ', silnia_v2(arg))
