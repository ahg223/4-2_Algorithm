def DFS(films,level,start,W,D,K,pos,i):
    global result
    if pos==level:
        a=check(films,W,D,K)
        if a:
            result = 1
            return
    for depth in range(start,D):
        tmp = films[depth]
        films[depth]=[i]*W
        DFS(films,level,depth+1,W,D,K,pos+1,i)
        if result:
            return
        films[depth]=tmp
        
def check(films,W,D,K):
    for row in range(W+1):
        if row == W:
            return True
        else:
            count=1
            before = films[0][row]
            for col in range(1,D+1):
                if col == D:
                    return False
                elif films[col][row]==before:
                    count+=1
                    if count>=K:
                        break
                else:
                    count=1
                    before=films[col][row]
         
     
T = int(input())
for test_case in range(1,T+1):
    print("#",end="")
    print(test_case, end=" ")
    D,W,K = map(int,input().split())
    films = [list(map(int,input().split())) for _ in range(D)]
    result = 0
    if K==1: print(result)
    else:
        for level in range(K+1):
            DFS(films,level,0,W,D,K,0,0)
            if result==1: break
            DFS(films,level,0,W,D,K,0,1)
            if result==1: break
        print(level)
