Coin = [500, 100, 50, 10, 5, 1]

Price = int(input())

change = 1000 - Price
answer = 0
for i in range(len(Coin)):
	if change < Coin[i]: continue
	else:
		answer += change // Coin[i]
		change -= Coin[i] * (change // Coin[i])

	if change == 0: break

print(answer)
