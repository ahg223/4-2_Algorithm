from sys import maxsize, setrecursionlimit, stdin
#input() = stdin.readline()
setrecursionlimit(10**8)
'''
N, Min = maxsize, maxsize
sequence = []

def recur(count, cal, indent, pre):
    global N
    global Min
    global sequence
    
    if count == N:
        if Min>cal: Min = cal
        return

    elif count == 0:
        for i in [0, -1, 1]: 
            if i == -1: cal += 1
            recur(count+1, cal, indent, sequence[0]+i)
    else:
        now = sequence[count]
        for i in [0, -1, 1]:
            now_indent = pre - now - i
            if i == -1: cal += 1
            if count == 1 or now_indent == indent: recur(count+1, cal, now_indent, now+i)

N = int(input())
sequence = list(map(int,input().split()))

recur(0, 0, 0, 0)
if Min == maxsize: print(-1)
else: print(Min)
'''

from sys import maxsize
N = int(input()) - 1
if N==0:
    print(0)
    exit() 
sequence = list(map(int,input().split()))
case = [[-1,-1,1], [0,-1,0], [1,-1,1], [-1,0,1], [0,0,0], [1,0,1], [-1,1,1], [0,1,0], [1,1,1]]
Min = maxsize


for i, j, count in case:
    first, last = sequence[0]+i, sequence[-1]+j
    step = (first - last)/N

    temp1, temp2 = first, 0
    for _ in range(1, N+1):
        Flag = False
        for K in [-1,0,1]:
            temp2 = sequence[_] + K
            if (temp1 - temp2) == step:
                Flag = True
                break
        if Flag:
            temp1 = temp2
            if K != 0: count+=1
        else: break
    
    if Flag == True and Min > count: Min = count

if Min == maxsize: print(-1)
else: print(Min)
