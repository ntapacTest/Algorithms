
def dfs(G, s, k, DFS):    
    
    for p in G[s]:
        if DFS.get(p)==None:
            k+=1
            DFS[p]=k            
            k=dfs(G, p, k, DFS)
    return k
    
# з пошуком найкоротшої відстані та шляху
def dfs_v2(G, s, k, DFS, D, P):    
    
    for p in G[s]:
        if DFS.get(p)==None:
            k+=1
            D[p]=(D[s])+1
            P[p]=s
            DFS[p]=k            
            k=dfs_v2(G, p, k, DFS, D, P)
    return k

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
dfs(G,'A',0,DFS)

print(DFS)


DFS_V2=dict()
# Найкоротша відстань
D=dict()
# Найкоротший шлях
P=dict()

DFS_V2['A']=0
D['A']=0

dfs_v2(G,'A',0,DFS_V2, D, P)
print(DFS_V2)
print(D)
print(P)