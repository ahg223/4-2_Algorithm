from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
q = []


def bfs():
    global q
    body, eat, ans = 2, 0, 0
    check = [[False] * n for _ in range(n)]
    while q:
        d, x, y = heappop(q)
        if 0 < a[x][y] < body:
            eat += 1
            a[x][y] = 0
            if eat == body:
                body += 1
                eat = 0
            ans += d
            d = 0
            q=[]
            check = [[False] * n for _ in range(n)]

        for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
            nd, nx, ny = d + 1, x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < a[nx][ny] > body or check[nx][ny]:
                continue
            check[nx][ny] = True
            heappush(q, (nd, nx, ny))
    print(ans)


for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            heappush(q, (0, i, j))
            a[i][j] = 0
bfs()

'''
Moving=[[1,0],[0,1],[-1,0],[0,-1]]
Min=1000000
Shark=0
def check(shark,Map):
    for i in range(N):
        for j in range(N):
            if Map[i][j]!=0 and Map[i][j]<shark[2]: return False
    return True

def moving(shark,Map,time):
    global Shark
    global Min
    if time>Min: return
    if check(shark,Map):
        if Min>time:
            Min=time
            print(Min)
        return

    for move in Moving:
        shark[0],shark[1]=shark[0]+move[0],shark[1]+move[1]
        print(shark,time)
        if len(Map)>shark[0]>-1 and len(Map)>shark[1]>-1:
            if Map[i][j]!=0 and Map[shark[0]][shark[1]]<shark[2]:
                Map[shark[0]][shark[1]]=0
                Shark+=1
                if Shark==shark[2]: Shark,shark[2]=0,shark[2]+1
            elif Map[shark[0]][shark[1]]>shark[2]:
                shark[0],shark[1]=shark[0]-move[0],shark[1]-move[1]
                continue
            moving(shark,Map,time+1)
        shark[0],shark[1]=shark[0]-move[0],shark[1]-move[1]


N=int(input())
Map=[[] for i in range(N)]
for i in range(N): Map[i].extend(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if Map[i][j]==9:
            shark,Map[i][j]=[i,j,2],0
            break

moving(shark,Map,0)
print(Min)

'''
