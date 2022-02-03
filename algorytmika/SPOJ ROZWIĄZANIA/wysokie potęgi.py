
a,b,c=map(int,input().split())
w=1
"""""
słaby sposób
for i in range(b):
    w=(w*a)%c
"""

def f(x,n,d):
    if n==0:
        return 1%d
    if n%2==1:
        return x*f(x,n-1)
    else:
        a=f(x,n/2)
        return (a**2)%d
print(f(a,b)%c)
