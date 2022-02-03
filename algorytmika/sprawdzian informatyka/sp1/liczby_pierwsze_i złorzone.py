

n=list(map(int,input().split()))

ff=[i for i in range(n[0],n[1]+1)]

g=[]
for i in range(n[0],n[1]):
    L = []


    ii = 2
    while ii * ii <= i:
        """" sprawdzamy dzielniki liczby n"""""
        while i % ii == 0:
            i /= ii
            L.append(i)
        ii += 1
    if i> 1: L.append(i)
    if len(L)==1:
        g.append(i)
for eli in g:
    if eli in ff:
        ff.remove(eli)
print(g)
print(ff)










