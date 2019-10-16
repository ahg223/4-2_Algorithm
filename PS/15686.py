import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def Calculation(chicken,house):
    dist=1000
    for _ in range(len(chicken)):
        i,j=chicken[_]
        I,J=house
        temp=abs(i-I)+abs(j-J)
        if dist>temp: dist=temp
    return dist

N,M=map(int,input().split())
Map=[list(map(int,input().split())) for i in range(N)]
Chicken=[]
House=[]
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1: House.append([i,j])
        elif Map[i][j] == 2: Chicken.append([i,j])

Case=combinations((i for i in range(len(Chicken))),M)

answer=100000
for cmd in Case:
    chicken,temp=[],0
    for _ in cmd: chicken.append(Chicken[_])
    for house in House:temp+=Calculation(chicken,house)
    if answer>temp: answer=temp
    
print(answer)
