import time
import timeit

file = open('dane1_4.txt', 'r')  # r do odczytu
A = []
# sposób I pętla
"""""
for i in range(1000):
    A.append(int(file.readline().strip()))
"""""




n=10000
A = list(map(int, file.readlines()))

maxsuma = A[0]
""""" 
pseudo kod by to zrobił
for p in range(0,n):
    for k in range(p,n):
        suma=0
        for i in range(p,k+1):
            suma=suma+A[i]
        if suma>maxsuma:
            maxsuma=suma
"""""
""""" trosdzke leprze z pytona
for p in range(0,n):
    for k in range(p,n):
        suma =sum(A[p:k+1])
        maxsuma=max(maxsuma,suma)

"""""
s=[]
suma_pref=0
for liczba in A:
    suma_pref+=liczba
    s.append(suma_pref)
s.append(0)
maxsum=0
for p in range(0,n):
    for k in range(p,n):
        suma=s[k]-s[p-1]
        if suma>maxsuma:
            maxsum=suma
            max_p=p
            max_k=k
print('maxsuma',maxsuma,'max_p',p,'max_k',k)

