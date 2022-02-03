

l=[1,4,3,7,6,2,9,11,5,0]
print(l)
i=0
while i<len(l)-1: #1=0
    idex=i #index=0
    j=i+1#j=i+1=0
    while j<len(l):
        if l[idex]>l[j]:
            idex=j
        j += 1
    l[i],l[idex]=l[idex],l[i]
    i+=1
    print(l)
"""""
pseudo kod
Dane:
n-liczba elementów
T[0,1,...n-1]
Wyniki:
posortowane T[0,1...n-1]
Dla i=0,1,..n-2:
    nr_min->i
    dla j=i+1,i+2..n-1 wykonaj:
        jeżeli T[j]<T[nr_min]:
            nr_min->j
        j->j+1
        p->T[j]
        t[j]->T[nr_min]
        T[nr_min]->p
złorzoność algorytmu 
n**2
y=0,5x**2-0,5*x
"""""