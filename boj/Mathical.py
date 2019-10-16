#2168
'''
n,m = map(int,input().split())

MAX, MIN = max(n,m), min(n, m)
number, divisor = MAX, MIN

while (number % divisor) != 0:
    remainder = number % divisor
    number = divisor
    divisor = remainder

print(int(( MAX/divisor + MIN/divisor -1) * divisor))
'''
#15965
'''
primary=[2]

K = int(input())
length = 1
Num=2
while K != length:
    Flag = True
    for num in primary:
        if Num % num == 0:
            Flag = False
            break
    if Flag:
        length+=1
        primary.append(Num)
    Num+=1
print(primary[-1])
'''
'''
k=int(input())
n=8000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
        
print(primes[k-1])
'''
#15995
'''
a, m = map(int, input().split())

Num=1
while True:
    Num += m
    if Num % a ==0:
        print(Num // a)
        break
   ''' 
#1476
'''
def Step2(Year, M):
    if M == 19 and Year % 19 ==0: return True
    elif Year % 19 ==M: return True
    else: return False

def Step3(Year, E):
    if E == 15 and Year % 15 ==0: return True
    elif Year % 15 == E: return True
    else: return False

E, S, M = map(int, input().split())

count=0
while True:
    Year = 28 * count + S

    #print(Year)
    if Step2(Year, M) and Step3(Year, E):
        print(Year)
        break
    count+=1
'''
#2149
'''
def MakeKey(KEY):
    TEMP, key = [], []
    for i in range(len(KEY)): TEMP.append([i, ord(KEY[i])])
    TEMP=sorted(TEMP, key= lambda x:x[1])
    for i in range(len(KEY)): key.append(TEMP[i][0])
    return key

KEY=input()
Before=input()

key=MakeKey(KEY) 
After=[[] for _ in range(len(key))]
Chunk = len(Before) // len(KEY)

for i in range(0, len(key)):
    Temp=Before[i * Chunk: (i+1) * Chunk]
    After[key[i]]=Temp

for j in range(Chunk):
    for i in range(len(After)):
        print(After[i][j], end="")
''' 
#11050
'''
m = 1000000007
 
def x_y(x, y):
    xy = 1
    while y > 0:
        if(y % 2) == 1:
            xy *= x
            y -= 1
            xy %= m
        x *= x
        x %= m
        y /= 2
    return xy
 
N, K = map(int, input().split())
 
r1 = 1
r2 = 1
 
for i in range(1, N+1):
    r1 *= i
    r1 %= m
 
for i in range(1, K+1):
    r2 *= i
    r2 %= m
 
for i in range(1, N-K+1):
    r2 *= i
    r2 %= m
 
r2 = x_y(r2, m-2)
r2 %= m
r1 *= r2
r1 %= m
print(r1)
'''
#11571
'''
MAX=1025
N = int(input())

for test_case in range(N):
    Memory=[0 for _ in range(MAX)]
    N, M = map(int, input().split())
    Answer = ""
    count = 0

    INTLEN=len(str(N//M))

    while True:
        count += 1
        
        i, j = N // M, N % M
        Answer += str(i)
        if Memory[j] != 0 or j==0: break
        else: Memory[j] = count
        N = j*10

    start, end = Memory[j]+INTLEN-1, count+INTLEN-1
    if INTLEN==1:    
        if j==0: print(Answer[0]+"."+Answer[1:]+"(0)")
        else: print(Answer[0]+"."+Answer[1:start]+"("+Answer[start:end]+")")
    else:
        if j==0: print(Answer[0:INTLEN]+"."+Answer[INTLEN:]+"(0)")
        else: print(Answer[0:INTLEN]+"."+Answer[INTLEN:start]+"("+Answer[start:end]+")")
'''
#4335
'''
memory=[0,11]
while True:
    num=int(input())
    if num==0: break
    feedback=input()
    
    if feedback=="too high" and memory[1]>num: memory[1]=num
    elif feedback=="too low" and memory[0]<num: memory[0]=num
    elif feedback=="right on":
        if memory[1] > num > memory[0]: print("Stan may be honest")
        else: print("Stan is dishonest")
        memory=[0,11]
'''     
#2014

from heapq import heappop, heappush

K, N = map(int,input().split())
Primes=list(map(int,input().split()))
heap=[]

for i in range(len(Primes)): heappush(heap, Primes[i])

for _ in range(N):
    Num=heappop(heap)
    print(Num, heap)
    for i in range(len(Primes)):
        heappush(heap, Num*Primes[i])
        if Num%Primes[i]==0: break
print(Num)

'''
import random

def m_search(m):
    count = 0
    for i in range(1, 10001):
        count+=1
        if i == m: break
        
    return count

def y_search(y):
    count=0
    first=1
    last=10000
    while first < last:
        count += 1
        mid = (first+last)//2
        if mid == y:
            break
        elif mid > y:
            last = mid-1
        elif mid < y:
            first = mid+1
    return count

m_win = 0
y_win = 0
for i in range(1000):
    m = random.randint(1,10000)
    y = random.randint(1,10000)
    m_win+=m_search(m)
    y_win+=y_search(y)

print("명륜이는 평균적으로 %d 시도 끝에 정답을 맞춥니다" %(m_win/1000))
print("율전이는 평균적으로 %d 시도 끝에 정답을 맞춥니다" %(y_win/1000))
'''
