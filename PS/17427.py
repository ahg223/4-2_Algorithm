Max = int(input())
Nums = []

Map = [1 for _ in range(Max+1)]
for i in range(2,Max+1):
    for _ in range(i,Max+1,i):
        Map[_]+=i

for i in range(1, Max): Map[i+1]+=Map[i]
print(Map[Max])
