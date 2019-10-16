
N = int(input())

Conference = [[] for i in range(N)]
for i in range(N): Conference[i] = list(map(int, input().split()))

Conference.sort(key = lambda x:(x[1],x[0]))

Answer = 1
Last=Conference[0][1]

for i in range(1,N):
	if Last<=Conference[i][0]:
		Last = Conference[i][1]
		Answer+=1
print(Answer)
