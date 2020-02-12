def sort(a,a1,an):
    
    if(an!=a1+1):  
        q=((an-a1)//2)+a1
        sort(a,a1,q)
        sort(a,q,an) 
        merge(a,a1,an,q)   
    
def merge(a,a1,an,q):
    l=[x for x in a[a1:q]]
    r=[x for x in a[q:an]]
     
    i=0
    j=0    
    for k in range(a1,an):
        if(i>=len(l)):
            a[k]=r[j]
            j+=1
        elif(j>=len(r)):
            a[k]=l[i]
            i+=1
        elif l[i]<=r[j]:
            a[k]=l[i]
            i+=1
        else:
            a[k]=r[j]
            j+=1

            

a=[12,1,3,6,2,6,8,0,233,64]
# a=[12,1,3,6]

sort(a,0,len(a))

print(a)