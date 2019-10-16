def moving(cell):
    if cell[3] ==1: return [cell[0]-1,cell[1],cell[2],cell[3]]
    elif cell[3] ==2: return [cell[0]+1,cell[1],cell[2],cell[3]]
    elif cell[3] ==3: return [cell[0],cell[1]-1,cell[2],cell[3]]
    elif cell[3] ==4: return [cell[0],cell[1]+1,cell[2],cell[3]]


T=int(input())

for test_case in range(1,T+1):
    print("#",end="")
    print(test_case,end=" ")
    N,M,K=map(int,input().split())
    
    Map=[[ [0,0] for i in range(N)] for j in range(N)]
    temp=[]
    for _ in range(K): temp.append(list(map(int,input().split())))

    for __ in range(M):
        Max=[[ 0 for i in range(N)] for j in range(N)]
        for _ in range(len(temp)): 
            X=moving(temp.pop())
            if Map[X[0]][X[1]][0] !=0: 
                Map[X[0]][X[1]][0]+=X[2]
                if Max[X[0]][X[1]]<X[2]:  Max[X[0]][X[1]], Map[X[0]][X[1]][1]=X[2] ,X[3]
            else: Map[X[0]][X[1]][0],Map[X[0]][X[1]][1],Max[X[0]][X[1]]=X[2],X[3],X[2]
        for i in range(N):
            for j in range(N):
                if (i==0 or j==0 or i==N-1 or j==N-1) and Map[i][j][0]!=0: 
                    Map[i][j][0]=Map[i][j][0]//2
                    if Map[i][j][1]==1: Map[i][j][1]=2
                    elif Map[i][j][1]==2: Map[i][j][1]=1
                    elif Map[i][j][1]==3: Map[i][j][1]=4
                    elif Map[i][j][1]==4: Map[i][j][1]=3
                if (i==0 or j==0) and Map[i][j][0]==0: Map[i][j]=[0,0]
        for i in range(N):
            for j in range(N):
                if Map[i][j][0] !=0:
                    temp.append([i,j,Map[i][j][0],Map[i][j][1]])
                    Map[i][j]=[0,0]
        
    sum=0
    for i in range(len(temp)): sum+=temp.pop()[2]
    
    print(sum)

