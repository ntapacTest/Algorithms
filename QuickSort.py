
def partition(a,p,r):
    x=a[r]
    i=p-1
    
    for j in range(p,r):

        if a[j]<=x:
            i+=1
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
            
    tmp=a[r]
    a[r]=a[i+1]
    a[i+1]=tmp
    return i+1

def sort(a,p,r):
    if(p<r):
        q=partition(a,p,r)
        sort(a,p,q-1)
        sort(a,q+1,r)

def quickSort(a):
    sort(a,0,len(a)-1)

a=[12,1,82,3,6,2,6,8,0,233,64]
# a = [2,1,8,3,1]

quickSort(a)

print(a)