#AL_06_01 - Reszta z dzielenia
""""""
for i in range(int(input())):
    num=list(map(int,input().split()))
    a=num[0]# losowa liczba (a)
    b=num[1]# losowy dzielnik (b)
    r=a%b
    if b < 0:  # sprawdzam czy liczba jest ujemna , i jeśli true
        b = -b
    if r>0:
        r=r+b

    print(r)


























