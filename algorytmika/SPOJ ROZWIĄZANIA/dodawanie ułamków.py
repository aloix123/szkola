
a=input().split()
u1=a[0]
u2=a[1]
nhehe='/'
w1=''
w3=''
w1f=[]
for i in range(len(u1)):
    if u1[i]==nhehe:
        w3=w3+' '+u1[i+1:]
        break
    w1+=u1[i]
w1f.append(w1)
w1f.append(w3)
v1_mianownik=int(w1f[1])
v1_ff=int(w1f[1])
v1_licznik=int(w1f[0])
v1_prli=int(w1f[0])
w2=''
w4=''
w2f=[]
for ii in range(len(u2)):
    if u2[ii]==nhehe:
        w4=w4+' '+u2[ii+1:]
        break
    w2+=u2[ii]
w2f.append(w2)
w2f.append(w4)
v2_mianownik=int(w2f[1])
v2_ff=int(w2f[1])
v2_licznik=int(w2f[0])
v2_prli=int(w2f[0])
def nwd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def nww(a, b):
    return (a * b) // nwd(a, b)
d=nww(v1_mianownik,v2_mianownik)
ile_coooo1=d/v1_mianownik
ile_coooo2=d/v2_mianownik
wynik=f'{u1} + {u2} = {int(ile_coooo2*v2_prli+ile_coooo1*v1_prli)}/{d}'
print(wynik)