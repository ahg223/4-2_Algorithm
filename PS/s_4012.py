def Tasty(answer,Map):
    temp,F1=[],0
    for i in range(len(answer)):
        for j in range(len(answer)):
            if i==j: continue
            else: temp.append([answer[i],answer[j]])
    for _ in temp:
        F1+=Map[_[0]][_[1]]

    temp,F2=[],0
    Answer=[i for i in range(len(Map))]
    for i in range(len(Answer)-1,-1,-1):
        if Answer[i] in answer: Answer.pop(i)
    
    for i in range(len(Answer)):
        for j in range(len(Answer)):
            if i==j: continue
            else: temp.append([Answer[i],Answer[j]])
    for _ in temp:
        F2+=Map[_[0]][_[1]]

    return abs(F1-F2)

from itertools import combinations

T= int(input())

for test_case in range(1,T+1):
    Min=10000000
    N=int(input())
    Map=[[]for i in range(N)]
    for i in range(N): Map[i].extend(list(map(int,input().split())))
    List=[i for i in range(N)]
    Answer=list(combinations(List,N//2))

    for answer in Answer:
        temp=Tasty(answer,Map)
        if Min>temp: Min=temp
    print(Min)
