'''
start,end=map(int,input().split())

sum=0
for i in range(start+1,end):
    if i%3==0 or i%5==0:sum+=1
print(sum)
'''
'''
Num=int(input())
Num1,Num2=Num,Num
Binary=''
Octat=''
while Num1!=0:
    Binary=str(Num1%2)+Binary
    Num1=Num1//2

while Num2!=0:
    Octat=str(Num2%8)+Octat
    Num2=Num2//8
print(Binary,Octat)
'''
'''
Num=int(input())

for i in range(Num):
    for j in range(Num-i): print(" ",end="")
    for j in range(i*2+1): print("*",end="")
    print("")
        
for i in range(Num-2,-1,-1):
    for j in range(Num-i): print(" ",end="")
    for j in range(i*2+1): print("*",end="")
    print("")
'''
'''
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
    pivot_val = x[lmark]
    pivot_idx = lmark
    while lmark <= rmark:
        while lmark <= rmark and x[lmark] <= pivot_val:
            lmark += 1
        while lmark <= rmark and x[rmark] >= pivot_val:
            rmark -= 1
        if lmark <= rmark:
            swap(x, lmark, rmark)
            lmark += 1
            rmark -= 1
    swap(x, pivot_idx, rmark)
    return rmark

def quickSort(x, pivotMethod=pivotFirst):
    def _qsort(x, first, last):
        if first < last:
            splitpoint = pivotMethod(x, first, last)
            _qsort(x, first, splitpoint-1)
            _qsort(x, splitpoint+1, last)
    _qsort(x, 0, len(x)-1)
    return x

List=list(map(int,input().split()))
print(quickSort(List))
'''
'''
def bs(a):
    if len(a) <= 1: return a
    p = a[0]
    left,mid,right=[],[],[]
    for i in a:
        if i == p:  mid.append(i)
        elif i < p: left.append(i)
        else:   right.append(i)
    return bs(left)+mid+bs(right)

a= [1,3,5,7,4,98,10,15,47,91,46,53,74,11]
print(bs(a))'''
'''
def SS(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]: a[i],a[j]=a[j],a[i]
    return a

a= [1,3,5,7,4,98,10,15,47,91,46,53,74,11]
print(SS(a))'''
'''
def QS(a):
    if len(a)<=1: return a
    left,mid,right=[],[],[]
    P=a[0]
    for i in range(len(a)):
        if a[i]>P: right.append(a[i])
        elif a[i]==P: mid.append(a[i])
        else: left.append(a[i])
    return QS(left)+mid+QS(right)
    
a= [1,3,5,7,4,98,10,15,47,91,46,53,74,11]
print(QS(a))
'''
'''
def BS(target,a,L,R):
    count=0
    while True:
        count+=1
        mid=(L+R)//2
        print(count)
        if a[mid]>target: R=mid-1
        elif a[mid]==target: return mid
        else: L=mid+1


a= [i for i in range(1000000)]
print(BS(int(input()),a,0,len(a)-1))
'''
'''
from itertools import permutations
W,Max = 6,0
item=[[3,7],[1,2],[2,4],[4,5]]
item2=[[3,7],[1,2],[2,4],[4,5]]
command=list(permutations([i for i in range(4)],4))
while command!=[]:
    Com=command.pop(0)
    weight=0
    value=0
    for i in Com:
        weight+=item[i][0]
        if weight>W: break
        value+=item[i][1]
    if value>Max: Max=value
print(Max)
'''
'''    
item=[[1,4,7],[1,2,8],[7,2,4],[7,3,5],[7,3,2],[4,5,5]]
lambda x:(x[0],x[1],x[2])
print(sorted(item,reverse=True,key=lambda x:(x[0],x[1],x[2])))
'''

import re

p=re.compile('[a-z] || ')
