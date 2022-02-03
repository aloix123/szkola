

def f(a,b):
    if a==b:
        return a
    else:
        s=f(a,b-1)+b
        return s


#lul , rozwiązanie w jednej linijce ezzzzzzzzzzzzzzzzz
print(sum([i for i in range(int(input("podaj liczbę a: ")),int(input("podaj liczbę b: "))+1)]))