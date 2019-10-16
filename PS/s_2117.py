def possible(i,j,P,_,Map):
    temp=0
    for n in range(-_+1,_):
        I=i+n
        for J in range(j-_+1+abs(n),j+_-abs(n)):
            if len(Map)>I>-1 and len(Map)>J>-1 and Map[I][J]==1: temp+=1
        if _ == abs(n):
            if len(Map)>I>-1 and len(Map)>J>-1 and Map[I][J]==1: temp+=1
    if temp>=P:return [True,temp]
    else: return [False,temp]

T=int(input())
for test_case in range(1,T+1):
    print("#",end="")
    print(test_case, end=" ")
    N,M=map(int,input().split())
    Map=[[]for i in range(N)]
    for i in range(N): Map[i]=list(map(int,input().split()))
        
    Flag=False
    temp=0
    for x in range(2*N,0,-1):
        P= 2*x**2 - 2*x + 1
        if P%M==0:P=P//M
        else: P=P//M+1
        for i in range(N):
            for j in range(N):
                [Flag,Temp]=possible(i,j,P,x,Map)
                if Flag and temp<Temp: temp=Temp
        if Flag:break
    print(temp)

