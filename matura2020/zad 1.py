k=int(input())
n=int(input())
A=[4, 2, 4, 4, 2, 6]
B=[4, 4, 2, 6, 4, 2]
k1=0
def
while k1<n:
    if k1<k:
        if A[k1]!=B[n-k+k1]:
            print("FAŁSZ")
    elif k1>k:
        if A[k1]!=B[k1-k]:
            print("FAŁSZ")
    k1+=1
    print(k1)
