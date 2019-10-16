
def AsciiArt(R,G,B):
    I = 2126*R + 7152*G + 722*B
    count = 510000

    if count>I: return "#"
    elif 2*count>I: return "o"
    elif 3*count>I: return "+"
    elif 4*count>I: return "-"
    else: return "."


N, M = map(int, input().split())
Map = [[0] * M for i in range(N)]

value = [[] for i in range(N)]

for i in range(N): value[i].extend(list(map(int, input().split())))

for i in range(N):
    for j in range(0,M*3,3):
        R,G,B = value[i][j:j+3]
        Map[i][j//3] = AsciiArt(R,G,B)


for i in range(N): 
    for j in range(M):print(Map[i][j], end="")
    print()
