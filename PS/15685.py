import copy

N=int(input())
Curve=[ list(map(int,input().split())) for i in range(N) ]

DragonCurve0={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
DragonCurve1={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
DragonCurve2={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
DragonCurve3={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[]}
DragonCurve=[DragonCurve0,DragonCurve1,DragonCurve2,DragonCurve3]
for i in range(11):
    if i==0:
        temp0=[[0,0],[1,0]]
        temp1=[[0,0],[0,-1]]
        temp2=[[0,0],[-1,0]]
        temp3=[[0,0],[0,1]]
    else:
        End=len(temp0)-1
        for j in range(len(temp0)-2,-1,-1):
            Temp0=[temp0[End][0]+(temp0[End][1]-temp0[j][1]),temp0[End][1]-(temp0[End][0]-temp0[j][0])]
            temp0.append(Temp0)
            Temp1=[temp1[End][0]+(temp1[End][1]-temp1[j][1]),temp1[End][1]-(temp1[End][0]-temp1[j][0])]
            temp1.append(Temp1)
            Temp2=[temp2[End][0]+(temp2[End][1]-temp2[j][1]),temp2[End][1]-(temp2[End][0]-temp2[j][0])]
            temp2.append(Temp2)
            Temp3=[temp3[End][0]+(temp3[End][1]-temp3[j][1]),temp3[End][1]-(temp3[End][0]-temp3[j][0])]
            temp3.append(Temp3)
    DragonCurve0[i].extend(temp0)
    DragonCurve1[i].extend(temp1)
    DragonCurve2[i].extend(temp2)
    DragonCurve3[i].extend(temp3)

Answer=[]
for _ in range(N):
    Temp=copy.deepcopy(DragonCurve[Curve[_][2]][Curve[_][3]])
    for dot in Temp: dot[0],dot[1]=dot[0]+Curve[_][0],dot[1]+Curve[_][1]
    Answer.extend(Temp)

Answer.sort()
for _ in range(len(Answer)-1,0,-1):
    if Answer[_]==Answer[_-1]: Answer.pop(_)

answer=0
for point0 in Answer:
    point1=[point0[0]+1,point0[1]]
    point2=[point0[0],point0[1]+1]
    point3=[point0[0]+1,point0[1]+1]
    if point1 in Answer and point2 in Answer and point3 in Answer: answer+=1
print(answer)
