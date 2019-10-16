from itertools import permutations
import copy
Min=0

def check(Map):
    count=0
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j]!=0: count+=1
    return count

def replacing(Map):
    for j in range(len(Map[0])):
        for i in range(len(Map)):
            if Map[i][j]==0: 
                for _ in range(i,0,-1): Map[_][j]=Map[_-1][j]
                Map[0][j]=0
    return Map

def breaking(j,Map):
    temp=[]
    for i in range(len(Map)):
        if Map[i][j]!=0:
            temp.append([i,j,Map[i][j]])
            break
    if temp==[]: return False
    while temp!=[]:
        #print(temp)
        item=temp.pop(0)
        for _ in range(item[2]):
            i,j=item[0],item[1]
            if _==0:
                Map[i][j]=0
                continue
            if len(Map)>i+_ and Map[i+_][j]!=0: 
                temp.append([i+_,j,Map[i+_][j]])
                Map[i+_][j]=0
            if i-_>-1 and Map[i-_][j]!=0: 
                temp.append([i-_,j,Map[i-_][j]])
                Map[i-_][j]=0
            if len(Map[0])>j+_ and Map[i][j+_]!=0: 
                temp.append([i,j+_,Map[i][j+_]])
                Map[i][j+_]=0
            if j-_>-1 and Map[i][j-_]!=0: 
                temp.append([i,j-_,Map[i][j-_]])
                Map[i][j-_]=0
        #for i in range(len(Map)): print(Map[i])
    return replacing(Map)

def recur(command,Map):
    global Min
    if Min==0: return
    Map2=copy.deepcopy(Map)
    for i in command:
        Map2=breaking(i,Map2)
        #for _ in range(len(Map2)):
        #    print(Map2[_])
        #print()
        if Map2==False: return
    total=check(Map2)
    if Min>total:
        Min=total
        print(command)
        for i in range(len(Map2)):print(Map2[i])
    
T = int(input())

for test_case in range(1, T + 1):
    print("#",end="")
    print(test_case,end=" ")
    N,W,H= map(int,input().split())
    Map=[list(map(int,input().split()))for i in range(H)]
    Max,Min=check(Map),W*H
    Temp=[i for i in range(W)]*N
    command=permutations(Temp,N)
    command=list(set(command))
    #print(sorted(command))
    #command=[2,2,6]
    #recur(command,Map)
    for i in command: recur(i,Map)
    print(Min)
