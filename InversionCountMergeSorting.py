def sort(a,a1,an):
    inv=0

    if(an!=a1+1):  
        q=((an-a1)//2)+a1
        inv+=sort(a,a1,q)
        inv+=sort(a,q,an)   
        # print(inv)     
        inv+=merge(a,a1,an,q)
        # print(inv)
        return inv
    return 0
    
def merge(a,a1,an,q):
    l=[x for x in a[a1:q]]
    r=[x for x in a[q:an]]
     
    i=0
    j=0
    inv=0    
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
            inv+=1
        
    return inv
            

# a=[12,1,3,6,2,6,8,0,233,64]
# a=[12,1,3,6,1,5]
a=[2,3,3,4,5,6]

inv=sort(a,0,len(a))

print(a, inv)