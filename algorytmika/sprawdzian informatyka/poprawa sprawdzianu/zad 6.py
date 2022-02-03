# n - liczba elementów
n=int(input())
T=list(map(int,input().split()))
ll=[]
for el in T:
    if el<0:
        el=-el
        ll.append(el)
    else:
        ll.append(el)
ll.sort()
for element in ll:
    i=0
    if T.__contains__(-element):
        element=T[i]
        i+=1
print(ll)