

lista=[21,33,17,24,31,4,27,20,18,7]
n=len(lista)

h=0
#p element początkowy
# k koncowy
def quiq(p,k):
    global h
    if  p<k:
        m=p
        for i in range(p+1,k+1):

            if lista[i]<lista[p]:
                m+=1
                ppp=lista[i]
                lista[i]=lista[m]
                lista[m]=ppp
            pp=lista[p]
            lista[p]=lista[m]
            lista[m]=pp

        quiq(p,m-1)
        quiq(m+1,k)
quiq(0,n-1)
print(lista)
