T=int(input())

for test_case in range(1,T+1):
    answer=0
    print("#",end="")
    print(test_case,end=" ")
    N,X=map(int,input().split())
    Map=[list(map(int,(input().split()))) for i in range(N)]
    
    
    flag=[[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        temp,length=100,0
        Flag=True
        for j in range(N):
            if temp==Map[i][j]: length+=1
            elif Map[i][j]==temp+1 and X<=length: 
                for _ in range(1,X+1): flag[i][j-_]=1
                temp,length= Map[i][j],1
            elif Map[i][j]>temp: Flag=False
            else: temp, length=Map[i][j],1
            if Flag==False:break
        
        temp,length=100,0
        for j in range(N-1,-1,-1):
            if flag[i][j]==1:temp,length=Map[i][j],0
            elif temp==Map[i][j]: length+=1
            elif Map[i][j]==temp+1 and X<=length: temp,length= Map[i][j],1
            elif Map[i][j]>temp: Flag=False
            else: temp, length=Map[i][j],1
            if Flag==False:break        
        if Flag: answer+=1
    
    flag=[[0 for i in range(N)] for i in range(N)]
    for j in range(N):
        temp,length=100,0
        Flag=True
        for i in range(N):
            if temp==Map[i][j]: length+=1
            elif Map[i][j]==temp+1 and X<=length: 
                for _ in range(1,X+1):flag[i-_][j]=1
                temp,length= Map[i][j],1
            elif Map[i][j]>temp: Flag=False
            else: temp, length=Map[i][j],1
            if Flag==False:break
                
        temp,length=100,0
        for i in range(N-1,-1,-1):
            if flag[i][j]==1:temp,length=Map[i][j],0
            elif temp==Map[i][j]: length+=1
            elif Map[i][j]==temp+1 and X<=length:  temp,length= Map[i][j],1
            elif Map[i][j]>temp: Flag=False
            else: temp, length=Map[i][j],1   
            if Flag==False:break
                
        if Flag: answer+=1
    print(answer)
