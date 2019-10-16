def checking(index,cell,locate,i):
    [I,J]=index
    if [I,J] not in locate:
        locate.append([I,J])
        cell.append([cell[i][0],0])
    else:
        Index=locate.index([I,J])
        if cell[Index][1]==0 and cell[i][0]>cell[Index][0]: cell[Index][0]=cell[i][0]

T = int(input())

for test_case in range(1, T + 1):
    print("#",end="")
    print(test_case, end=" ")
    N,M,K=map(int,input().split())
    Map=[[] for i in range(N)]
    for i in range(N):Map[i].extend(list(map(int,input().split())))
    locate=[]
    cell=[]
    for i in range(N):
        for j in range(M):
            if Map[i][j]!=0: 
                locate.append([i,j])
                cell.append([Map[i][j],0])
    
    for _ in range(K):
        #print(_,len(locate))
        for i in range(len(cell)):
            if 2*cell[i][0]>cell[i][1]: cell[i][1]+=1
            elif 2*cell[i][0]==cell[i][1]: continue
        for i in range(len(cell)):
            if cell[i][0]+1==cell[i][1]:
                [I,J]=locate[i]
                checking([I+1,J],cell,locate,i)
                checking([I-1,J],cell,locate,i)
                checking([I,J+1],cell,locate,i)
                checking([I,J-1],cell,locate,i)
        
    answer=len(cell)
    #print(locate)
    for i in cell:
        if 2*i[0]==i[1]:answer-=1
    print(answer)
