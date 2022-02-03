n=int(input())
T=list(map(int,input().split()))
A=[]
B=[]
for i in range(n//2+2):
    A.append(0)
    B.append(0)

# n - liczba elementów
# p - nr początkowego elementu
# k - nr koncowego ele`mentu (włącznie)

def scalaj(p, s, k):
    for i in range(p, s+1):
        A[i-p]=T[i]
    A[s-p+1]=1000000000

    for i in range(s+1, k+1):
        B[i-(s+1)]=T[i]
    B[k-s]=1000000000

    a=0 # nr elementu w liście A
    b=0 # nr elementu w liście B
    for i in range(p, k + 1):

        if A[a] < B[b]:
            T[i] = A[a]
            a += 1

        else:
            T[i] = B[b]
            b += 1

def sortuj_przez_scalanie(p,k):
    if p<k:
        s=(p+k)//2
        sortuj_przez_scalanie(p,s)
        sortuj_przez_scalanie(s+1,k)
        scalaj(p,s,k)


sortuj_przez_scalanie(0, n-1)
print(*T)