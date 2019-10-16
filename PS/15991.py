Test_case = int(input())
Answer = []
for _ in range(Test_case): Answer.append(int(input()))

Num = max(Answer)+1
Sheet = [[0,0,0] for _ in range(Num)]


def AnswerSheet():
        Sheet[1], Sheet[2], Sheet[3] = [1,0,0], [1,1,0], [1,0,1]
        Sheet[4], Sheet[5], Sheet[6] = [2,1,0], [2,1,0], [3,2,1]
        if 7>Num: return

        for i in range(7, Num):
                Sheet[i][0] = (Sheet[i-2][0] + Sheet[i-2][1] + Sheet[i-2][2])%1000000009
                Sheet[i][1] = (Sheet[i-4][0] + Sheet[i-4][1] + Sheet[i-4][2])%1000000009
                Sheet[i][2] = (Sheet[i-6][0] + Sheet[i-6][1] + Sheet[i-6][2])%1000000009
AnswerSheet()
for _ in range(Test_case): print((Sheet[Answer[_]][0]+Sheet[Answer[_]][1]+Sheet[Answer[_]][2])%1000000009)
