import copy

Dir={1:[[0,1]], 2:[[0,1],[0,-1]], 3:[[-1,0],[0,1]], 4:[[-1,0],[1,0],[0,1]], 5:[[-1,0],[1,0],[0,-1],[0,1]] }

N, M = map(int, input().split())
CCTV = []
Min=1000


def DFS(Map, CCTV, depth):
    global Min

    if depth ==-1:
        count=0
        for i in range(N):
            for j in range(M):
                if Map[i][j]==0: count+=1
        if count < Min:
            Min=count
            #for i in range(N): print(Map[i])
        return

    cmds=Dir[CCTV[depth][2]]
    for _ in range(4):
        temp=copy.deepcopy(cmds)
        MMap=copy.deepcopy(Map)
        cmds=[]
        i, j, value = CCTV[depth]
        for x, y in temp: cmds.append([y, -x])
        for x, y in cmds: MMap=moving(MMap, i, j, x, y)
        #for __ in range(N): print(MMap[__])

        DFS(MMap, CCTV, depth-1)



def moving(Map, i, j, x, y):
    #print(x, y)
    if x == 1:
        while True:
            if i != N-1 and Map[i + 1][j] != 6:
                i += 1
                if Map[i][j] == 0: Map[i][j] = -1
            else: break

    elif x == -1:
        while True:
            if i != 0 and Map[i - 1][j] != 6:
                i -= 1
                if Map[i][j] == 0: Map[i][j] = -1
            else: break

    elif y == 1:
          while True:
              if j != M-1 and Map[i][j + 1] != 6:
                  j += 1
                  if Map[i][j] == 0: Map[i][j] = -1
              else:  break

    elif y == -1:
         while True:
             if j != 0 and Map[i][j-1] != 6:
                 j -= 1
                 if Map[i][j] == 0: Map[i][j] = -1
             else: break
    return Map


Map=[ list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if Map[i][j]!=0 and Map[i][j] != 6:  CCTV.append([i,j,Map[i][j]])

DFS(Map, CCTV, len(CCTV)-1)
print(Min)
