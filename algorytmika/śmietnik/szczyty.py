n=int(input())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))
#Żadne dwa szczyty nie leżą w jednej linii z obserwatorem.
Punkty=[]
for punkt in range(len(X)):
    Punkty.append([X[punkt],Y[punkt]])

s=9999999# skrajnie lewy punkt
lewo=[]#element skrajnie po lewo
for element in Punkty:


    stosunek_e=element[0]/element[1]


    lewo.append(stosunek_e)
lewo.reverse()
print(lewo)
for i in range(n):
    for j in range(n-1):
        if lewo[j]>lewo[j+1]:
            p=lewo[j]
            lewo[j]=lewo[j+1]
            lewo[j+1]=p
print(lewo)
"""""
4
-2 1 3 2
2 3 4 1

x=X[i]
y=Y[i]
Dla i = 1,2,3..i wykonaj:
    Dla j = 1,2,3..i wykonaj:
        Jeżeli X[j]/Y[j]<Y[j+1]/Y[j+1] wtedy:
            p=X[j]
            X[j]=X[j+1]
            X[j+1]=p
            g=Y[j]
            Y[j]=Y[j+1]
            Y[j+1]g
"""

