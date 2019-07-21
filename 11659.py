
N, M = map(int, input().split())

Num = list(map(int, input().split()))
Sum = [0 for _ in range(N)]

Sum[0] = Num[0]
for i in range(N):
	Sum[i] = Sum[i-1] + Num[i]

Sum.insert(0,0)
for _ in range(M):
	start, end = map(int, input().split())
	print(Sum[end]-Sum[start-1])
