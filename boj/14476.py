def GCD(a, b):
	while b>0: a, b = b, a%b
	return a

N = int(input())
Num = list(map(int, input().split()))
Num.insert(-1, Num[-1])
Num.insert(0, Num[0])

LtoR = [0 for _ in range(N+2)]
RtoL = [0 for _ in range(N+2)]
LtoR[0] = Num[0]
RtoL[N+1] = Num[N+1]

for i in range(1,N+1):
	j = N + 1 - i
	LtoR[i]=GCD(LtoR[i-1],Num[i])
	RtoL[j]=GCD(RtoL[j+1],Num[j])

answer, MAX = 0, 0
LtoR[0] = RtoL[2]
RtoL[N+1] = LtoR[N-1]
for i in range(1,N+1):
	temp = GCD(LtoR[i-1],RtoL[i+1])
	if temp>MAX: answer, MAX = i, temp

if Num[answer]%MAX == 0: print(-1)
else: print(MAX, Num[answer])
