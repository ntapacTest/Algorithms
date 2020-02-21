   
S=[]

DFS=dict()
# Найкоротша відстань
D=dict()
# Найкоротший шлях
P=dict()

G={
    'A':['B','C'],
    'B':['D','E'],
    'C':['E','G'],
    'D':['F'],
    'E':['F'],
    'F':['G'],
    'G':[]
}


DFS['A']=0
S.append('A')
k=0

while len(S)!=0:

    s=S[-1]
    
    k+=1
    p= list(G.keys())[k]

    if p in G[s] and DFS.get(p)==None:
        DFS[p]=k
        S.append(p)
    else:
        S.remove(P)
        


print(DFS)