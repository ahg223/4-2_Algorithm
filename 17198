
'''
Map=[input() for _ in range(10)]
Map.insert(0,'0000000000')
Map.append('0000000000')
for i in range(12): 
	Map[i]= '0' + Map[i]
	Map[i]+='0'

start, end, rock = [], [], []
answer = 100000

def printMap(Map):
	for i in range(1,11): print(Map[i][1:-1])
	print()

def Moving(i,j,length):
	printMap(Map)
	if Map[i][j] == '0' or [i,j] in rock: return
	if [i,j] == end[0]:
		if length<answer: answer=length
		print(answer)
		return

	rock.append([i,j])
	Map[i] = Map[i][:j] + "C"+ Map[i][j+1:]
	Moving(i+1,j,length+1)
	Moving(i-1,j,length+1)
	Moving(i,j+1,length+1)
	Moving(i,j-1,length+1)
	Map[i] = Map[i][:j] + "."+ Map[i][j+1:]
	rock.pop()

for i in range(1,11):
	for j in range(1,11):
		if Map[i][j] == 'L': start.append([i,j])
		elif Map[i][j] == 'R': rock.append([i,j])
		elif Map[i][j] == 'B': end.append([i,j])

[a,b] = start[0]
Moving(a,b,0)

print(answer)
'''


dy = [-1,1,0,0]
dx = [0,0,-1,1]
Map=[input() for _ in range(10)]

Flag = False
for i in range(1,11):
	for j in range(1,11):
		if Map[i][j] == 'B': Flag=True
		if Flag: break
	if Flag: break

def bfs(i,j):
	queue=[[i,j,0]]
	visited=[[False for _  in range(10)] for __ in range(10)]
	visited[i][j]=True
	
	while queue!=[]:
		x ,y, length = queue.pop()
		if Map[x][y] == "L": return length - 1
		
		for _ in range(4):
			Nx, Ny = x+dx[_], y+dy[_]
			if not (10>=Nx>0 and 10>=Ny>0): continue
			if not (visited[Ny][Nx] or Map[Ny][Nx]=="R"): continue

			queue.append([Ny, Nx, length+1])
			visited[Ny][Nx] = True
print(bfs(i, j))
	

print(answer)
