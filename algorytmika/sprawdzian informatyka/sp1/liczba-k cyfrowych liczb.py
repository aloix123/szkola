
# kombinatoryka lewel hard
for i in range(int(input())):
    l=list(map(int,input().split()))
    k=l[0]
    n=l[1]

    if k==1:print(n)
    else:
        l=n-1
        for h in range(1,k):
            l*=n
        print(l)












