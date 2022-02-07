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

"""""
moje rozwiązanie 
resultTotal=0
indexlisty=0
totalhelper=0
while indexlisty<len(A):


    liczba=A[indexlisty]
    if liczba>0:
        totalhelper += liczba

    if liczba<0:
        totalhelper += liczba
        if totalhelper<0:
            totalhelper=0

    if totalhelper>resultTotal:
        resultTotal=totalhelper
    indexlisty += 1
"""""
n=len(A)
max_suma=0
max_p=0
max_k=0
p=0
k=0
suma=0
while p<n and k<n:
    suma+=A[k]
    if suma<0:
        p=k+1
        k=p
        suma=0
    elif suma>max_suma:
        max_suma=suma
        max_p=p
        max_k=k
        k+=1
    else:
        k+=1


print(str(max_p)+' '+str(max_k))



##print('maxsuma',maxsuma,'max_p',p,'max_k',k)

