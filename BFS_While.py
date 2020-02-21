

def bfs(G,s):
    pass


Q=[]

BFS=dict()
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

k=0
Q.append('A')
BFS['A']=k

D['A']=0


while len(Q)!=0:

    s=Q[0]
    for p in G[s]:
        if(BFS.get(p)==None):
            k+=1
            D[p]=(D[s])+1
            P[p]=s
            BFS[p]=k            
            Q.append(p)
            
    Q.pop(0)


print(BFS)
print(D)
print(P)

    