

ex_list=[2,1,5,6,9,7]
print(f'krok startowy{ex_list}')
l=len(ex_list)
i=1
while i<l:#i=4
    kej=ex_list[i] #5
    j=i-1 #1
    while j>=0 and kej<ex_list[j]:

        ex_list[j+1]=ex_list[j]

        j-=1
    ex_list[j+1]=kej
    i+=1
    print(f'krok={i-1} {ex_list}')

