
import  sys
B=['B','-','-','-','-']
C=['C','-','-','-','-']
A=['A',4,3,2,1]
def printer():
    print(A[4],B[4],C[4])
    print(A[3],B[3],C[3])
    print(A[2],B[2],C[2])
    print(A[1],B[1],C[1])
    print(A[0],B[0],C[0])
printer()

def AB():
    "in this function I'm just transport tower hanoi's puck between list A and B"
    n = -1
    m = 0
    while A[n]=='-':
        n+=-1
    while B[m]!='-':
        m+=1
    #replecing
    if type(B[m-1])==int :
        if B[m-1]<A[n]:
            print("ERRRRRROTRRRR, CAN NOT ADD BRO, NUMBER ")
    else:
        B[m] = A[n]
        A[n] = '-'
        printer()
def BA():
    "in this function I'm just transport tower hanoi's puck between list A and B"
    n = -1
    m = 0
    while B[n]=='-':
        n+=-1
    while A[m]!='-':
        m+=1
    #replecing

    A[m] = B[n]
    B[n] = '-'

    if type(A[m-1])==int :
        if A[m-1]<B[n]:

            print("ERRRRRROTRRRR, CAN NOT ADD BRO, NUMBER ")

    else:
        A[m] = B[n]
        B[n] = '-'
        printer()
def AC():
    "in this function I'm just transport tower hanoi's puck between list A and B"
    n = -1
    m = 0
    while A[n]=='-':
        n+=-1
    while C[m]!='-':
        m+=1
    #replecing
    if type(C[m-1])==int :
        if C[m-1]<A[n]:
            print("ERRRRRROTRRRR, CAN NOT ADD BRO, NUMBER ")
    else:
        C[m] = A[n]
        A[n] = '-'
        printer()
def CA():
    "in this function I'm just transport tower hanoi's puck between list A and B"
    n = -1
    m = 0
    while C[n]=='-':
        n+=-1
    while A[m]!='-':
        m+=1
    #replecing
    if type(A[m-1])==int :
        if A[m-1]<C[n]:
            print("ERRRRRROTRRRR, CAN NOT ADD BRO, NUMBER ")
    else:
        A[m] = C[n]
        C[n] = '-'
        printer()
while True:
    afasd = input().upper()
    if afasd=='AB':
        AB()
    if afasd=='AC':
        AC()
    if afasd=='CA':
        CA()
    if afasd=='Q':
        sys.exit(0)





