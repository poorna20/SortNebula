a=[[1,5],[2,4],[1,3],[9,0]]
n=4 #Number of rows
print ("Matrix before sorting: ")
for i in range (0,n):
    for j in range (0,2):
        print (a[i][j],end=' ')
    print ()

def gnomesort(a,n): #n being number of rows
    ind=0
    while ind<n:
        if ind==0: #Going to the right element
            ind=ind+1
        if a[ind][0]>a[ind-1][0]: #Checking if the previous element is smaller, if true incrementing index by 1
            ind=ind+1
        elif a[ind][0]==a[ind-1][0] and a[ind][1]<a[ind-1][1]: #If the Previous element is equal, Checking the value elements
            a[ind][0],a[ind-1][0]=a[ind-1][0],a[ind][0]
            a[ind][1],a[ind-1][1]=a[ind-1][1],a[ind][1]
            ind=ind+1        
        
        else:
            a[ind][0],a[ind-1][0]=a[ind-1][0],a[ind][0]
            a[ind][1],a[ind-1][1]=a[ind-1][1],a[ind][1]
            ind=ind-1

    return a



a=gnomesort(a,n)
print ("Sorted Matrix: ")
for i in range (0,n):
    for j in range (0,2):
        print (a[i][j],end=' ')
    print ()

    


