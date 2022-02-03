l=input()# niepotrzebne
lista=list(map(int,input().split()))

def mergesort(list):
    if len(list)>1:
        middle=len(list)//2
        Right=list[middle:]
        Left=list[:middle]
        mergesort(Left)
        mergesort(Right)

        i=k=j=0
        while i<len(Left) and j<len(Right):
            if Left[i]<Right[j]:
                list[k]=Left[i]
                i+=1
            else:
                list[k]=Right[j]
                j+=1
            k+=1
        while i<len(Left):
            list[k]=Left[i]
            i+=1 ;k+=1

        while j< len(Right):
            list[k]=Right[j]
            j+=1;k+=1

        print(list)
mergesort(lista)
""""
func mergesort( var a as array )
     if ( n == 1 ) return a

     var l1 as array = a[0] ... a[n/2]
     var l2 as array = a[n/2+1] ... a[n]

     l1 = mergesort( l1 )
     l2 = mergesort( l2 )

     return merge( l1, l2 )
end func

func merge( var a as array, var b as array )
     var c as array

     while ( a and b have elements )
          if ( a[0] > b[0] )
               add b[0] to the end of c
               remove b[0] from b
          else
               add a[0] to the end of c
               remove a[0] from a
     while ( a has elements )
          add a[0] to the end of c
          remove a[0] from a
     while ( b has elements )
          add b[0] to the end of c
          remove b[0] from b
     return c
"""""