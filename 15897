

N = int(input())
sum, step = 0, 0
i=1
while N>=i:
	divide, rem = (N-1)//i, (N-1)%i
	if divide == 0: step = 1
	else: step = rem//divide + 1
	sum += (1+(N-1)//i) * step
	i+=step

print(sum)

