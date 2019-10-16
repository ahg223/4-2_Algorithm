Memory = [0,1]

N = int(input())

if N>1:
	for _ in range(N-1): Memory.append(Memory[-1]+Memory[-2])

print(Memory[-1])
