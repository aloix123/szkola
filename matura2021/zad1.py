num=input()
print(num)
def transform(num):

    lista=[]
    for element in range(len(num)):
        lista.append(num[element])
    lista=list(map(int,lista))
    return lista
def odwracaj(arrya):
    result=''
    for liczba in arrya:
        realnum=9-liczba
        result+=str(realnum)
    print(result)
fact=transform(num)
odwracaj(fact)