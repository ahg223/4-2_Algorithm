def moving(now,dir):
    if dir==0: return now
    elif dir==1: return now[0]-1,now[1]
    elif dir==2: return now[0],now[1]+1
    elif dir==3: return now[0]+1,now[1]
    else: return now[0],now[1]-1

def MAX(Adir,Bdir,BC):
    Amax,Bmax,maybe=[],[],[]
    i,j=0,0
    for bc in BC:
        Adis=abs(Adir[0]-bc[0])+abs(Adir[1]-bc[1])
        Bdis=abs(Bdir[0]-bc[0])+abs(Bdir[1]-bc[1])
        if bc[2]>=Adis and bc[2]>=Bdis: maybe.append(bc[3])
        elif bc[2]>=Adis: Amax.append(bc[3])
        elif bc[2]>=Bdis: Bmax.append(bc[3])
    if len(Amax)>0:i=max(Amax)
    if len(Bmax)>0:j=max(Bmax)
    Max=i+j
    for _ in maybe:
        List=[[i,_],[_,j]]
        for k in List:
            if Max<k[0]+k[1]: Max,i,j=k[0]+k[1],k[0],k[1]
    return i+j

T = int(input())

for test_case in range(1, T + 1):
    print("#",end="")
    print(test_case,end=" ")
    answer=0
    M,A=map(int,input().split())
    Adir,Bdir,BC=[[1,1]],[[10,10]],[]
    tmp=list(map(int,input().split()))
    for i in range(M): Adir.append(moving(Adir[-1],tmp[i]))
    tmp=list(map(int,input().split()))
    for i in range(M): Bdir.append(moving(Bdir[-1],tmp[i]))
    for i in range(A): 
        BC.append(list(map(int,input().split())))
        BC[-1][0],BC[-1][1]=BC[-1][1],BC[-1][0]
    
    for i in range(M+1): answer+=MAX(Adir[i],Bdir[i],BC)
    print(answer)
