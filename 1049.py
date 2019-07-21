N,M = map(int, input().split())
Answer=[]

Package, Solo = 10000, 10000
for _ in range(M):
	i1, i2 = map(int, input().split())
	if Solo>i2: Solo=i2
	if Package>i1 and i2>i1/6: Package=i1

	
print(min((N//6+1)*Package, (N//6)*Package + (N%6)*Solo, N*Solo))
