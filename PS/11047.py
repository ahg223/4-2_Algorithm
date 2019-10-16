
N, K = map(int, input().split())

Coin = []
for i in range(N): Coin.append(int(input()))

Answer = 0

for i in range(N-1,-1,-1):
	if Coin[i]>K: continue
	else: 
		Answer += K // Coin[i]
		K -= Coin[i] * (K // Coin[i])
	if not K: break
	#print(K, Coin[i])


print(Answer)
