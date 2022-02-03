

result=''
def sym(a,b):
    global result
    if a>0:
        sym(a-1,b+1)
        result+=str(a*b)
        sym(a-1,b+1)
sym(4,4)
print(len(result))
#ŹLE TO JEST