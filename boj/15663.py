'''
from itertools import permutations

_, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()


def unique(iterable):
    Temp=set()
    for x in iterable:
        if x in Temp: continue
        else: Temp.add(x)
    return Temp

for seq in unique(permutations(nums, m)):
    print(' '.join(str(x) for x in seq))
'''
N, M= 0, 0
Final, Memoization, Data=[], [], []
def combination(Flag, Answer, start):
    global Final
    global Memoization
    global Data
    global N
    if Flag==0: Final.append(Answer)

    else:
        for i in range(start, N):
            combination(Flag-1, Answer+str(Data[i])+" ", i)

N, M= map(int,input().split())
Memoization=[0 for _ in range(N)]
Data=list(map(int,input().split()))
Data = list(set(Data))
Data.sort()
N= len(Data)
combination(M, "", 0)
for _ in range(len(Final)): print(Final[_])

