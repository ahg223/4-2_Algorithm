import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N,L,R=map(int,input().split())
Map=[list(map(int, input().split())) for i in range(N)]
Union=[]
Dir=[[1,0],[-1,0],[0,1],[0,-1]]
Visited=[[False]*N for _ in range(N)]

def Check(i,j):
    Visited[i][j]=True
    Union.append([i,j])
    for x,y in Dir:
        I,J=x+i,y+j
        if N>I>-1 and N>J>-1 and Visited[I][J]==False and R+1>abs(Map[i][j]-Map[I][J])>L-1: Check(I,J)


answer=-1
Flag=True
while Flag:
    answer+=1
    if N==1: break
    Flag=False
    Visited=[[False]*N for _ in range(N)]
    #for i in range(N): print(Map[i])
    for i in range(N):
        for j in range(N):
            if Visited[i][j]==False: Check(i,j)
            if len(Union)>1:
                #print(Union)
                Sum,Flag=0,True
                for I,J in Union: Sum+=Map[I][J]
                for I,J in Union: Map[I][J]=Sum//len(Union)
            Union=[]

print(answer)
