dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
blocks = {1: (1, 3, 0, 2), 2: (3, 0, 1, 2), 3: (2, 0, 3, 1), 4: (1, 2, 3, 0), 5: (1, 0, 3, 2)}

def play(board, y, x, dir):
    cur_y, cur_x = y, x
    score = 0
    while True:
        ny, nx = cur_y + dy[dir], cur_x + dx[dir]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            if dir == 0:    dir = 1
            elif dir == 1:  dir = 0
            elif dir == 2:  dir = 3
            else:           dir = 2
            score += 1
        else: cur_y, cur_x = ny, nx

        if board[cur_y][cur_x] in [1,2,3,4,5]:
            dir = blocks[board[cur_y][cur_x]][dir]
            score += 1
            
        if board[cur_y][cur_x] in [6,7,8,9,10]:
            for wy, wx in wormhole[board[cur_y][cur_x]]:
                if (wy, wx) != (cur_y, cur_x):
                    cur_y, cur_x = wy, wx
                    break
            
        if board[cur_y][cur_x] == -1: return score
        if cur_y == y and cur_x == x: return score

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0 for x in range(N)] for y in range(N)]
    wormhole = {i: [] for i in range(6, 11)}
    for y in range(N):
        board[y] = list(map(int, input().split()))
        for x in range(N):
            v = board[y][x]
            if v in [6,7,8,9,10]: wormhole[v].append((y,x))

    max_score = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                for d in range(4):
                    score = play(board, y, x, d)
                    if score > max_score: max_score = score

    print("#{} {}".format(test_case, max_score))

'''
Map,Init,WARM=[0,0],[],[0,0,0,0,0,0,[],[],[],[],[]]
Max=0
def start(Map):
    global WARM
    START=[]
    for i in range(N+2):
        for j in range(N+2):
            if Map[i][j]>5: WARM[Map[i][j]].append([i,j])
            elif Map[i][j]==0: 
                temp=[[i,j]]
                if Map[i+1][j]!=-1:temp.append([1,0])
                if Map[i-1][j]!=-1:temp.append([-1,0])
                if Map[i][j+1]!=-1:temp.append([0,1])
                if Map[i][j-1]!=-1:temp.append([0,-1])
                START.append(temp)
    print(START)
    return START

def moving(START,Dir,score):
    global Max
    I,J=START[0]+Dir[0],START[1]+Dir[1]
    print(I,J)
    if I>N+1 or 0>I or J>N+1 or 0>J: return
    elif (Init[0]==I and Init[1]==J) or Map[I][J]==-1: 
        if score>Max: Max=score
        return
    
    if Map[I][J]==1 and Dir[0]==1 and Dir[1]==0: score,Dir[0],Dir[1]=score+1,0,1
    elif Map[I][J]==1 and Dir[0]==0 and Dir[1]==1: score,Dir[0],Dir[1]=score+1,1,0
    elif Map[I][J]==2 and Dir[0]==-1 and Dir[1]==0: score,Dir[0],Dir[1]=score+1,0,1
    elif Map[I][J]==2 and Dir[0]==0 and Dir[1]==1: score,Dir[0],Dir[1]=score+1,-1,0
    elif Map[I][J]==3 and Dir[0]==-1 and Dir[1]==0: score,Dir[0],Dir[1]=score+1,0,-1
    elif Map[I][J]==3 and Dir[0]==0 and Dir[1]==-2: score,Dir[0],Dir[1]=score+1,-1,0
    elif Map[I][J]==4 and Dir[0]==1 and Dir[1]==0: score,Dir[0],Dir[1]=score+1,0,1
    elif Map[I][J]==4 and Dir[0]==0 and Dir[1]==1: score,Dir[0],Dir[1]=score+1,1,0
    elif Map[I][J] in [6,7,8,9,10] : 
        for i in range(2):
            if WARM[Map[I][J]][i][0]==I and WARM[Map[I][J]][i][1]==J: continue
            else: I,J=WARM[Map[I][J]][i][0],WARM[Map[I][J]][i][1]
    elif Map[I][J]!=0: 
        score+=1
        if  Dir[0]==0 and Dir[1]==1: Dir[0], Dir[1]=0,-1
        elif  Dir[0]==0 and Dir[1]==-1: Dir[0], Dir[1]=0,1
        elif  Dir[0]==1 and Dir[1]==0: Dir[0], Dir[1]=-1,0
        elif  Dir[0]==-1 and Dir[1]==0: Dir[0], Dir[1]=1,0
        
    
    moving([I,J],Dir,score)
    

T = int(input())

for test_case in range(1, T + 1):
    #print("#",end="")
    #print(test_case,end=" ")
    N=int(input())
    Map=[[] for i in range(N)]
    for i in range(N): Map[i].extend(list(map(int,input().split())))
    Map.insert(0,[5 for i in range(N)])
    Map.insert(N+1,[5 for i in range(N)])
    for i in range(N+2): 
        Map[i].insert(0,5)
        Map[i].append(5)

    START=start(Map)
    
    for init in START:
        Init[0],Init[1]=init[0][0],init[0][1]
        for i in range(1,len(init)):
            score=0
            moving(init[0],init[i],score)
    print(Max)
'''
