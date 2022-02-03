
a,b,c,s=map(int,input().split())

s=s*100
def nwd(a,b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a
def nww(a,b):
    return(a*b)//nwd(a,b)
d=nww(a,nww(b,c))
print(s//d)
