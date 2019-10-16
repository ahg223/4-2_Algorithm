#!/usr/bin/env python
# coding: utf-8

# 전역 변수

# In[1]:


Graph=[[0 for j in range(100)] for i in range(100)]
Graph_value=[0 for i in range(100)]
BFSvisit=[0 for i in range(100)]
queue=[0 for i in range(100)]


# Queue print 함수

# In[2]:


def print_Queue(front, rear):
    global Graph
    global Graph_value
    global BFSvisit
    global queue
    print()
    while True:
        if front==rear: break
        print("%d "%Graph_value[queue[front]],end=" ")
        front=front+1


# BFS 함수

# In[3]:


def BFS(v, N, Result):
    global Graph
    global Graph_value
    global BFSvisit
    global queue
    front=0
    rear=0
    
    print("%d "%v,end=" ")
    queue[0]=v
    rear+=1
    BFSvisit[v]=1
    while(front<rear):
        pop=queue[front]
        front+=1
        print("pop: %d"%Graph_value[pop])
        if pop==Result: break
        
        for i in range(1,N+1):
            if Graph[pop][i]==1 and BFSvisit[i]==0:
                queue[rear]=i
                rear+=1
                BFSvisit[i]=1
        print_Queue(front,rear)


# 메인 함수

# In[4]:


print("노드의 숫자, edge의 갯수, 시작하는 노드의 숫자를 순서대로 입력해주세요")
print("노드는 0번은 없고 1번부터 시작합니다. 숫자는 1000 이하의 숫자이어야 합니다")
N=int(input("노드의 숫자"))
M=int(input("edge의 개수"))
Start=int(input("시작하는 노드 인덱스"))

for i in range(1,M+1):
    x=int(input("edge의 양 끝 노드의 인덱스를 입력하세요. 노드는 1번부터 시작합니다"))
    y=int(input("edge의 양 끝 노드의 인덱스를 입력하세요. 노드는 1번부터 시작합니다"))
    print("Graph[%d][%d]에 edge가 생겼습니다"%(x,y))
    Graph[x][y]=1
    Graph[y][x]=1
    
for i in range(1,N+1):
    Graph_value[i]=int(input(" %d 번째 노드의 값을 입력하세요\n 단 0은 입력할 수 없습니다\n"%i))

Result=int(input("찾는 값을 입력해주세요"))
BFS(Start,N,Result)

