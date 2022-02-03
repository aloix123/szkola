v = input().split()
while len(v) != 0:
    j = int(v[0])
    w = list(map(int,v[1:]))
    w.sort(reverse=True)
    k=1
    m=1
    while m<len(w) and k!=j:
        if w[m]<w[m-1]:
            k+=1
        m+=1

    if k==j:
        print(w[m-1])
    else:
        print('-')
    try:
        v = input().split()
    except EOFError:
        break

"""""
3 10 20 30
4 10 20 30 30
2 1 2 6 8 9
1 16 16 18
"""""
