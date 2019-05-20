a=[[2,4],[9,0],[1,3],[1,5]]
n=4
print ("Matrix before sorting: ")
for i in range(0,n):
    for j in range(0,2):
        print (a[i][j], end=' ')
    print ()



def cocktailsort(a,n):
    swapped= True
    start=0
    end=n-1
    while (swapped==True):
        swapped=False
        for i in range (start,end):
            if(a[i][0]>a[i+1][0]):
                a[i][0],a[i+1][0]=a[i+1][0],a[i][0]
                a[i][1],a[i+1][1]=a[i+1][1],a[i][1]
                swapped=True
            elif (a[i][0]==a[i+1][0] and a[i][1]>a[i+1][0]):
                a[i][1],a[i+1][1]=a[i+1][1],a[i][1]
                swapped=True


        if (swapped==False):
            break
        swapped=False
        end=end-1
        for i in range(end-1,start-1,-1):
            if (a[i][0]>a[i+1][0]):
                a[i][0],a[i+1][0]=a[i+1][0],a[i][0]
                a[i][1],a[i+1][1]=a[i+1][1],a[i][1]
                swapped=True
            elif (a[i][0]==a[i+1][0] and a[i][1]>a[i+1][1]):
                a[i][1],a[i+1][1]=a[i+1][1],a[i][1]

        start=start+1

cocktailsort(a,n)
print ("Sorted Array is: ")
for i in range(0,n):
    for j in range(0,2):
        print (a[i][j], end=' ')
    print ()
                
                
                
