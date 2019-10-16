import copy
import itertools

N, M, H = map(int, input().split())

def cmd_maker(_):
    column, row = [i for i in range(N - 1)], [i for i in range(H)]
    columns = itertools.permutations(column*_, _)
    rows = itertools.permutations(row*_, _)
    cmds=[]

    for a in columns:
        for b in rows:
            cmds.append([a, b])

    return cmds


def simulation(MMap, cmd):
    if cmd is not []:
        print(cmd)
        for a, b in cmd:
            for i in a:
                for j in b:
                    if MMap[i][j] is False and MMap[i][j+1] is False:
                        MMap[i][j], MMap[i][j+1] = True, True
                    else: return False

    StartPoint=[[0, _] for _ in range(len(MMap)) ]

    for i, j in StartPoint:
        Arrive = j
        while i != H:
            if j != 1 and MMap[i][j] == True and MMap[i][j - 1] == True:
                j -= 1
            elif j != N and MMap[i][j] == True and MMap[i][j + 1] == True:
                j += 1
            i += 1
        if Arrive != j: return False
    return True


Map = [[False] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    Map[a][b], Map[a][b + 1] = True, True

Flag = False
for _ in range(4):
    if _ is 0:
        MMap = copy.deepcopy(Map)
        if simulation(MMap, []): Flag = False
    else:
        cmds = cmd_maker(_)
        print(cmds)
        for cmd in cmds:
            if Flag: break
            MMap = copy.deepcopy(Map)
            #if simulation(MMap, cmd):Flag = False
    if Flag: break

if Flag is False:
    print(-1)
else:
    print(_)

'''
N,M,H=map(int,input().split())
StartPoint=[[1,i] for i in range(1,N+1)]
Line=[]
for _ in range(M): Line.append(list(map(int,input().split())))
Ladder=[[False]*(N+1) for i in range(H+1)]
for i,j in Line: Ladder[i][j],Ladder[i][j+1]=True,True

def Check(Ladder):
    for i,j in StartPoint:
        Arrive=j
        while i!=H+1:
            if j!=1 and Ladder[i][j]==True and Ladder[i][j-1]==True: j-=1
            elif j!=N+1 and Ladder[i][j]==True and Ladder[i][j+1]==True: j+=1
            i+=1
        if Arrive!=j: return False
    return True

Possible=[]
for i in range(1,H+1):
    for j in range(1,N):
        if Ladder[i][j]==False and Ladder[i][j+1]==False: Possible.append([i,j]) 

Flag=False
for i in range(len(Possible)):
    Command=combinations((_ for _ in range(len(Possible))), i)    
    for cmd in Command:
        ladder=deepcopy(Ladder)
        for j in cmd:
            I,J=Possible[j]
            if ladder[I][J]==False and ladder[I][J+1]==False: ladder[I][J],ladder[I][J+1]=True,True
        if Check(ladder):
            print(i)
            Flag=True
        if Flag: break
    if Flag:break
if Flag==False: print(-1)
'''
