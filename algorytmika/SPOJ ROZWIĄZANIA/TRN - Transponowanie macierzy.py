

sdef=list(map(int,input().split()))
m=sdef[0]# ilość wierszy
n=sdef[1]# długość wierszy
r=[]
for i in range(m):
    f=list(map(int,input().split()))
    r.append(f)
for d in range(n):
    s=''
    for i in range(m):
        s+=str(r[i][d])
    print(*s)

#
# 4 3
# 1 2 5
# 4 3 3
# 3 4 9
# 8 7 7
