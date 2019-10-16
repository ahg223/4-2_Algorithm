'''
Square = []
square1, square2, square3 = list(map(int, input().split())) ,list(map(int, input().split())) ,list(map(int, input().split()))
Square = square1 + square2 + square3

max, Temp, Flag = 0, 0, False
for i in range(len(Square)):
    if Square[i]>Temp:
        max = i
        Temp = Square[i]

L = Square[max]

count = 0
for i in [2,4,6]:
    if Square[i-2:i].count(L)==1: count+=1

if count>1:
    length = 0
    T = []
    for i in range(6):
        if Square[i] == L and i%2==0: 
            length+=Square[i+1]
            T.extend([i,i+1])
        elif Square[i] == L and i%2==1: 
            length+=Square[i-1]
            T.extend([i-1,i])
    for i in range(6):
        if i not in T and Square[i] == length: Flag=True
print(T,L)

order=[0,1,2,3,4,5]
if max%2==0:
    order.pop(max)
    order.pop(max)
else:
    order.pop(max-1)
    order.pop(max-1)

temp = []
for i in order[:2]:
    for j in order[2:]:
        if Square[i] == Square[j]: temp.append([i,j])

if len(temp)==1:
    length=0
    for i in order:
       if i not in temp[0]: length += Square[i]
    if length == L: Flag=True

elif len(temp)==2:
    Length=0
    Temp = list(set(temp[0]+temp[1]))
    if len(Temp)==3:
        F=True
        for i in order:
            if i not in Temp: Length+=Square[i]
            elif F:
                Length+=Square[i]
                F=False
        if Length == L: Flag = True
 
    elif len(Temp)==4:
        for i in order:
            if Square[i] == L/2:
                Flag=True
                break

elif len(temp)==4:
    if Square[temp[0][0]] == L/2: Flag=True

for L in Square:
    if L in square1 and L in square2 and L in square3: Flag=True

if Flag: print("YES")
else: print("NO")
''''''

first, second, third = list(map(int,input().split())), list(map(int,input().split())), list(map(int,input().split()))

first.sort(reverse=True)
second.sort(reverse=True)
third.sort(reverse=True)

sortedArr = [first, second, third]

sortedArr.sort(reverse=True)

a,b,c,d,e,f = sortedArr[0][0], sortedArr[0][1], sortedArr[1][0], sortedArr[1][1], sortedArr[2][0], sortedArr[2][1]

flag = False
if a-b==c:
	if a-b==f:
		if a==d+e:
			flag = True
	if a-b==e:
		if a==d+f:
			flag = True
elif a-b==d:
	if a-b==f:
		if a==c+e:
			flag = True
	if a-b==e:
		if a==c+f:
			flag = True
			
if flag:
	print("YES")
else:
	print("NO")
'''

def swap(a, b):
    return (a, b) if a > b else (b, a)


def li():
    return swap(*map(int, input().split()))


sortedArr = sorted([li() for i in range(3)])[::-1]
(a, b), (c, d), (e, f) = tuple(sortedArr)

flag = False
if a == b+c:
    if b+f == d+e == a:
        flag = True
    if b+e == d+f == a:
        flag = True
elif a == b+d:
    if b+f == c+e == a:
        flag = True
    if b+e == c+f == a:
        flag = True


print("YES" if flag else "NO")
