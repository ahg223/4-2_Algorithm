from sys import stdin
from collections import deque
input = stdin.readline

ans = 0
dx, dy = (-1, -1, -1, 0, 0, 1, 1, 1), (-1, 0, 1, -1, 1, -1, 0, 1)
N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
nutrient = [[5 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    ans += 1

def spring_summer():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if nutrient[i][j] >= tree[i][j][k]:
                    nutrient[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    while k < len(tree[i][j]):
                        nutrient[i][j] += (tree[i][j].pop()//2)
                        ans -= 1
                    break

def fall_winter():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k]%5 == 0:
                    for t in range(8):
                        x, y = i+dx[t], j+dy[t]
                        if x < 0 or x >= N or y < 0 or y >= N:
                            continue
                        tree[x][y].appendleft(1)
                        ans += 1
            nutrient[i][j] += a[i][j]

def solve():
    for _ in range(K):
        spring_summer()
        fall_winter()
    print(ans)

solve()

'''
def spring(Map,Tree):
    Tree=sorted(Tree,key = lambda x:x[2])
    for tree in Tree:
        if Map[tree[0]][tree[1]]>=tree[2]:
            Map[tree[0]][tree[1]]-=tree[2]
            tree[2]+=1
        else: tree[3]=False 
    
def summer(Map,Tree):
    for i in range(len(Tree)-1,-1,-1):
        if Tree[i][3]==False:
            Map[Tree[i][0]][Tree[i][1]]+=Tree[i][2]//2
            Tree.pop(i)

def fall(Map,Tree):
    Dir=[[-1,-1],[-1,0],[-1,+1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for tree in Tree:
        if tree[2]%5==0:
            for move in Dir:
                temp=[tree[0],tree[1],1,True]
                temp[0],temp[1]=temp[0]+move[0],temp[1]+move[1]
                if len(Map)>temp[0]>-1 and len(Map)>temp[1]>-1: Tree.append(temp)

def winter(Map,Nourish):
    for i in range(len(Map)):
        for j in range(len(Map)): Map[i][j]+=Nourish[i][j]

N,M,K=map(int,input().split())
Tree=[]
Map=[[5 for i in range(N)] for i in range(N)]
Nourish=[[] for i in range(N)]
for i in range(N): Nourish[i].extend(map(int,input().split()))

for i in range(M):
    temp=list(map(int,input().split()))
    temp[0],temp[1]=temp[0]-1,temp[1]-1
    temp.append(True)
    Tree.append(temp)

for i in range(K):
    spring(Map,Tree)
    summer(Map,Tree)
    fall(Map,Tree)
    winter(Map,Nourish)

print(len(Tree))
'''
'''
import heapq
import copy

def spring(Map,Tree):
    for tree in Tree:
        if Map[tree[1]][tree[2]]>=tree[0]:
            Map[tree[1]][tree[2]]-=tree[0]
            tree[0]+=1
        else: tree[3]=False 
    
def summer(Map,Tree):
    for i in range(len(Tree)-1,-1,-1):
        if Tree[i][3]==False:
            Map[Tree[i][1]][Tree[i][2]]+=Tree[i][0]//2
            Tree.pop(i)

def fall(Map,Tree):
    Dir=[[-1,-1],[-1,0],[-1,+1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    Temp=copy.deepcopy(Tree)
    for tree in Tree:
        if tree[0]%5==0:
            for move in Dir:
                temp=[1,tree[1],tree[2],True]
                temp[1],temp[2]=temp[1]+move[0],temp[2]+move[1]
                if len(Map)>temp[1]>-1 and len(Map)>temp[2]>-1: heapq.heappush(Temp,temp)
    return Temp

def winter(Map,Nourish):
    for i in range(len(Map)):
        for j in range(len(Map)): Map[i][j]+=Nourish[i][j]

N,M,K=map(int,input().split())
Tree=[]
Map=[[5 for i in range(N)] for i in range(N)]
Nourish=[[] for i in range(N)]
for i in range(N): Nourish[i].extend(map(int,input().split()))

for i in range(M):
    temp=list(map(int,input().split()))
    Temp=[temp[2],temp[0]-1,temp[1]-1,True]
    heapq.heappush(Tree,Temp)

for i in range(K):
    spring(Map,Tree)
    summer(Map,Tree)
    Tree=fall(Map,Tree)
    winter(Map,Nourish)
    
print(len(Tree))
'''
