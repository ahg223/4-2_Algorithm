N = int(input())

Num1 = []
Num2 = []

for _ in range(N):
	a, b = map(int, input().split())
	Num1.append(a)
	Num2.append(b)

MAX = max(Num1)+1
Sheet = [[0]*_ for _ in range(MAX)]

def AnswerSheet():
	Sheet[1] = [1,0,0]
	Sheet[2] = [1,1,0]
	Sheet[3] = [1,2,1]

	for i in range(4, MAX):
		for j in range(1,4):
			for x in range(len(Sheet[i-j])):
				Sheet[i][x+1]+=Sheet[i-j][x]

AnswerSheet()

for i in range(N): print(Sheet[Num1[i]][Num2[i]-1]%1000000009)
