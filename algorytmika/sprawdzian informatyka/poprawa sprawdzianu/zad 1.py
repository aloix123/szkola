l=[21,33,17,24,31,4,27,20,18,7]
i=0
while i<len(l)-1: #1=0
    idex=i #index=0
    j=i+1#j=i+1=0
    while j<len(l):
        if l[idex]>l[j]:
            idex=j
        j += 1
    l[i],l[idex]=l[idex],l[i]
    i+=1
    print(l)



