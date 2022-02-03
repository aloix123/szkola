

for i in range(int(input())):
    num=input().split()
    a=int(num[0])
    b=int(num[1])


    def nwd(a, b):
        while b != 0:
            c = a % b
            a = b
            b = c
        return a


    def nww(a, b):
        return (a * b) // nwd(a, b)
    print(nww(a,b))

