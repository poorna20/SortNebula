a=[[1,5],[2,4],[1,3],[9,0]] #Taking the given example as a matrix (Not asking user for values).


#Considering a single row, both the element as one entity. Sorting them first
def partition(a,low,high):
 
    i=(low-1)
    pivot =a[high][0]
    for j in range(low, high):
        if a[j][0]<pivot: #Comparing elements with Pivot which is the last element if it is smaller than or equal to pivot
            i=i+1
            a[i][0],a[j][0]=a[j][0],a[i][0]
            a[i][1],a[j][1]=a[j][1],a[i][1]
        elif (a[j][0]==pivot and a[j][1]<a[high][1]):  #The Case when both the keys are equal
            i=i+1
            a[i][0],a[j][0]=a[j][0],a[i][0]
            a[i][1],a[j][1]=a[j][1],a[i][1]

                       
    a[i+1][0],a[high][0]=a[high][0],a[i+1][0]
    a[i+1][1],a[high][1]=a[high][1],a[i+1][1]
    return (i+1)
    

def quicksort(a,low,high):
  
    if low<high:
        pi=partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)

print ("Matrix before sorting: ")
for i in range (0,4):
    for j in range(0,2):
        print (a[i][j],end=' ')
    print ()
quicksort(a,0,3)
print ("After: ")
for i in range (0,4):
    for j in range(0,2):
        print (a[i][j],end=' ')
    print ()





    
