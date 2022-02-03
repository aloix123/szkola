ex_list=[2,1,6,9,5,7]
n=len(ex_list)
for i in range(n-2,-1,-1):
    x=ex_list[i]
    p=i
    k=n
    while k-p>1:
        j=(p+k)//2
        if x<=ex_list[j]:
            k=j
        else:
            p=j
    for j in range(i,p):
        ex_list[j]=ex_list[j+1]
    ex_list[p]=x
print(ex_list)