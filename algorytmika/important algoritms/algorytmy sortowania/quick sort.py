
lista=[1,4,3,7,6,2,9,11,5,0]
print(f'krok statrtowy{lista}')
def  quick(l):
    if len(l)<=1:
        return l
    pivot = l.pop(0)
    smaller_list=[]
    bigger_list=[]
    for i in l:
        if i>pivot:
            bigger_list.append(i)
        else:
            smaller_list.append(i)
    print(lista)
    return quick(smaller_list)+[pivot]+quick(bigger_list)
print(quick(lista))



