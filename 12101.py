from copy import deepcopy
Num = 12
Sheet = [[] for _ in range(Num)]


def AnswerSheet():
        Sheet[1], Sheet[2], Sheet[3] = [[1]], [[1,1],[2]], [[1,1,1],[1,2],[2,1],[3]]
        
        for i in range(4, Num):
                for _ in range(len(Sheet[i-1])):
                        temp = deepcopy(Sheet[i-1][_])
                        temp.insert(0,1)
                        Sheet[i].append(temp)
                for _ in range(len(Sheet[i-2])): 
                        temp = deepcopy(Sheet[i-2][_])
                        temp.insert(0,2)
                        Sheet[i].append(temp)
                for _ in range(len(Sheet[i-3])):
                        temp = deepcopy(Sheet[i-3][_])
                        temp.insert(0,3)
                        Sheet[i].append(temp)
 

AnswerSheet()
N,M = map(int,input().split())

#Sheet[7].sort(key = lambda x:len(x), reverse=True)
for _ in Sheet[7]: print(_)

if len(Sheet[N]) < M: print(-1)
else:
        answer=""
        M-=1
        Sheet[N].sort(key = lambda x:len(x), reverse=True)
        for _ in Sheet[N][M]: answer+= str(_) +"+"
        print(answer[:-1])
