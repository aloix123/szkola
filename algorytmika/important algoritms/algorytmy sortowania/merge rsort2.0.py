n=int(input())
tab=map(int,input().split())

A=[]
B=[]
for i in range(n//2+2):
    A.append(0)
    B.append(0)
def scalaj(s,p,k):
    A=tab[p:s]
    B=tab[s+1:k]
    b=0
    a=0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            tab[k] = B[a]
            a += 1
        else:
            tab[k] = B[b]
            b += 1
        k += 1
def s(p,k):
    if p<k:
        s=int(p+k//2)
        s(p,s)
        s(s+1,k)
        scalaj(s,p,k)
print(s(0,n))