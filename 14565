N, A = map(int,input().split())
print(N-A,end=" ")
r1, r2, t1, t2 = N, A, 0, 1
while r2>0:
	#print(r1,r2,t1,t2)
	q = r1//r2
	r0,t0 = r1-q*r2, t1-q*t2
	r1,r2 = r2,r0
	t1,t2 = t2,t0
if r1==1 and t1>=0: print(t1)
elif r1==1: print((N+t1)%N)
else: print(-1)
