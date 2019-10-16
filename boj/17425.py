from math import sqrt

T = int(input())

Max = 0
Nums = []
for _ in range(T):
    temp = int(input())
    if temp> Max: Max=temp
    Nums.append(temp)

Map = [1 for _ in range(Max+1)]
for i in range(2,Max+1):
    for _ in range(i,Max+1,i):
        Map[_]+=i

for i in range(1, Max): Map[i+1]+=Map[i]

for i in Nums: print(Map[i])
