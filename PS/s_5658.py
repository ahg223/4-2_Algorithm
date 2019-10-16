def Octat(Num):
    oct,answer=1,0
    for i in range(len(Num)-1,-1,-1):
        if Num[i]=="A": temp=10
        elif Num[i]=="B": temp=11
        elif Num[i]=="C": temp=12
        elif Num[i]=="D": temp=13
        elif Num[i]=="E": temp=14
        elif Num[i]=="F": temp=15
        else: temp=Num[i]
        answer+=int(temp)*oct
        oct*=16
    return answer

def Shifting(num1,num2,num3,num4):
    Num1=num4[-1]+num1[:-1]
    Num2=num1[-1]+num2[:-1]
    Num3=num2[-1]+num3[:-1]
    Num4=num3[-1]+num4[:-1]
    return Num1,Num2,Num3,Num4
    

T = int(input())

for test_case in range(1, T + 1):
    N,K=map(int,input().split())
    n=N//4
    temp=str(input())
    num1=temp[:n]
    num2=temp[n:2*n]
    num3=temp[2*n:3*n]
    num4=temp[3*n:]

    Answer=[]
    for _ in range(n):
        Answer.append(Octat(num1))
        Answer.append(Octat(num2))
        Answer.append(Octat(num3))
        Answer.append(Octat(num4))
        num1,num2,num3,num4=Shifting(num1,num2,num3,num4)

    Answer=sorted(list(set(Answer)),reverse=True)
    #print(Answer)
    print("#{} {}".format(test_case,Answer[K-1]))
