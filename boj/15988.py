
Test_case = int(input())
Answer = []
for _ in range(Test_case): Answer.append(int(input()))

Num = max(Answer)+1
Sheet = [0 for _ in range(Num)]


def AnswerSheet():
	Sheet[1], Sheet[2], Sheet[3] = 1, 2, 4
	
	for i in range(4, Num):
		Sheet[i] = Sheet[i-1] + Sheet[i-2] + Sheet[i-3]
		Sheet[i] %= 1000000009

AnswerSheet()
for _ in range(Test_case): print(Sheet[Answer[_]])
