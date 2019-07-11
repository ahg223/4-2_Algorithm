N, K = map(int,input().split())
Known = [int(x) for x in input().split()]

angles = [[0]*361 for i in range(N+1)]


def Angles(count, angle):
    if angles[count][angle] == 1: return
    if count == N: return
    
    angles[count][angle] = 1
    Angles(count, (360+angle+Known[count])%360)
    Angles(count, (360+angle-Known[count])%360)
    Angles(count+1, angle)


Angles(0,0)

temp = [int(x) for x in input().split()]
for i in range(K):
    if angles[-2][temp[i]] == 1 : print("YES")
    else: print("NO")

'''
N, K = map(int,input().split())
Known = list(map(int, input().split()))
angles = [[0 for _ in range(361)] for __ in range(11)]
ans=[0 for _ in range(361)]

def Angle(count,angle):
        if angles[count][angle]!=0:return
        if count == N: return

        angles[count][angle]=1
        ans[angle]=1
        next1, next2 = (angle + Known[count] + 360)%360, (angle - Known[count] + 360)%360

        Angle(count, next1)
        Angle(count, next2)
        Angle(count+1, angle)


Angle(0,0)

'''
for i in range(11):
        for j in range(361):
                if angles[i][j]: print(j, end=" ")
        print()
'''

temp=list(map(int,input().split()))
for _ in range(K):
        if ans[temp[_]]!=0: print("YES")
        else: print("NO")
'''
