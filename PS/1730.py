
N = int(input())
commands = input()
Map = [["."]*N for _ in range(N)]
i, j = 0, 0
for cmd in commands:
    if cmd =="U" and i!=0:
        if Map[i][j] == ".": Map[i][j] ="|"
        elif Map[i][j] == "-": Map[i][j] ="+"
        if Map[i-1][j] == ".": Map[i+-1][j] ="|"
        elif Map[i-1][j] == "-": Map[i-1][j] ="+"
        i-=1
    elif cmd =="D" and i!=N-1:
        if Map[i][j] == ".": Map[i][j] ="|"
        elif Map[i][j] == "-": Map[i][j] ="+"
        if Map[i+1][j] == ".": Map[i+1][j] ="|"
        elif Map[i+1][j] == "-": Map[i+1][j] ="+"
        i+=1
    elif cmd =="R" and j!=N-1:
        if Map[i][j] == ".": Map[i][j] ="-"
        elif Map[i][j] == "|": Map[i][j] ="+"
        if Map[i][j+1] == ".": Map[i][j+1] ="-"
        elif Map[i][j+1] == "|": Map[i][j+1] ="+"
        j+=1
    elif cmd =="L" and j!=0:
        if Map[i][j] == ".": Map[i][j] ="-"
        elif Map[i][j] == "|": Map[i][j] ="+"
        if Map[i][j-1] == ".": Map[i][j-1] ="-"
        elif Map[i][j-1] == "|": Map[i][j-1] ="+"
        j-=1

for i in range(N): 
    for j in range(N):print(Map[i][j],end="")
    print()
