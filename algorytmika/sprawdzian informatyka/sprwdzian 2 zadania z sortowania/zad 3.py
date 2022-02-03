ex_list=[21,33,17,24,31,4,27,20,18,7]
i=0
flaga=True

while i<len(ex_list)-1 and flaga:
    j=0
    flaga=False
    while j<len(ex_list)-1-i:
        if ex_list[j]>ex_list[j+1]:
            ex_list[j],ex_list[j+1]=ex_list[j+1],ex_list[j]

            flaga=True
        j += 1
    i+=1
    print(f'krok{i}:{ex_list}')