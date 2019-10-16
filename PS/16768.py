Dir = [[1,0],[-1,0],[0,1],[0,-1]]


N,K = map(int, input().split())

count = 0
Map, Memoization = [], []
for _ in range(N): Map.append(list(input()))

Memoization = [[0 for i in range(10)] for j in range(N)]

def DFS(i,j,color):
    global Map
    global Memoization
    global count
    for d1, d2 in Dir:
        i_, j_ = i+d1, j+d2
        if N>i_>-1 and 10>j_>-1 and Memoization[i_][j_] == 0 and Map[i_][j_]==color:
            Memoization[i_][j_] = 1
            count+=1
            DFS(i_,j_,color)

def gravity():
    global N
    global Map

    for j in range(10):
        for i in range(N-2,-1,-1):
            for k in range(i+1,N):
                if Map[k][j] == 0:
                    Map[k-1][j], Map[k][j] = Map[k][j], Map[k-1][j]

Flag = True
while Flag:
    Flag = False
    for i in range(N):
        for j in range(10):
            if Map[i][j]==0 or Memoization[i][j] == 1: continue
            count = 0
            Memoization = [[0 for i in range(10)] for j in range(N)]
            DFS(i,j,Map[i][j])
            if count >= K:
                Flag = True
                for i_ in range(N):
                    for j_ in range(10):
                        if Memoization[i_][j_] == 1: Map[i_][j_] = 0

    gravity()

for i in range(N): 
    for j in range(10):
        print(Map[i][j], end="")
    print()
